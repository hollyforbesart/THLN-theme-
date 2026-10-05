<?php
/**
 * Page layout.
 *
 * A page built from THLN patterns is a "canvas" page: full width, no Astra
 * title or sidebar, each section running edge to edge. Every other page and
 * all blog posts keep Astra's normal layout with THLN fonts and colors.
 */

defined( 'ABSPATH' ) || exit;

function thln_is_canvas() {
	static $is = null;
	if ( null !== $is ) {
		return $is;
	}
	$is = false;
	if ( is_singular( 'page' ) ) {
		$post = get_queried_object();
		$is   = $post instanceof WP_Post && false !== strpos( $post->post_content, 'thln-section' );
	}
	return $is;
}

add_filter( 'astra_get_content_layout', 'thln_canvas_content_layout', 99 );
function thln_canvas_content_layout( $layout ) {
	return thln_is_canvas() ? 'page-builder' : $layout;
}

add_filter( 'astra_page_layout', 'thln_canvas_sidebar', 99 );
function thln_canvas_sidebar( $layout ) {
	return thln_is_canvas() ? 'no-sidebar' : $layout;
}

add_filter( 'astra_the_title_enabled', 'thln_canvas_title', 99 );
function thln_canvas_title( $enabled ) {
	return thln_is_canvas() ? false : $enabled;
}

add_filter( 'body_class', 'thln_body_class' );
function thln_body_class( $classes ) {
	$classes[] = 'thln';
	if ( thln_is_canvas() ) {
		$classes[] = 'thln-canvas';
	}
	return $classes;
}

/**
 * WordPress gives every block inside a "flow" group a 24px top margin and no
 * bottom margin. THLN sections use the design system's own spacing instead,
 * so the flow class is removed from everything inside a THLN section.
 */
add_filter( 'render_block_core/group', 'thln_strip_flow_layout', 10, 2 );
function thln_strip_flow_layout( $html, $block ) {
	$cls = isset( $block['attrs']['className'] ) ? $block['attrs']['className'] : '';
	if ( false === strpos( $cls, 'thln-section' ) ) {
		return $html;
	}
	return preg_replace( '/(?<![\w-])is-layout-flow(?![\w-])/', 'thln-flow', $html );
}
