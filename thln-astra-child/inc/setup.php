<?php
/**
 * Theme setup: menus, assets, editor styles, block styles, pattern categories.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'after_setup_theme', 'thln_setup', 20 );
function thln_setup() {
	register_nav_menus(
		array(
			'thln-footer-explore' => __( 'Footer: Explore', 'thln' ),
			'thln-footer-legal'   => __( 'Footer: The fine print', 'thln' ),
		)
	);

	// Make the block editor look like the live site.
	add_theme_support( 'editor-styles' );
	add_editor_style( array( 'assets/css/thln-reset.css', 'assets/css/thln.css', 'assets/css/thln-wp-editor.css', 'assets/css/editor.css' ) );
}

add_action( 'wp_enqueue_scripts', 'thln_enqueue_assets', 20 );
function thln_enqueue_assets() {
	$deps = wp_style_is( 'astra-theme-css', 'registered' ) ? array( 'astra-theme-css' ) : array();
	wp_enqueue_style( 'thln-reset', THLN_URI . '/assets/css/thln-reset.css', $deps, THLN_VERSION );
	wp_enqueue_style( 'thln', THLN_URI . '/assets/css/thln.css', array( 'thln-reset' ), THLN_VERSION );
	wp_enqueue_style( 'thln-wp', THLN_URI . '/assets/css/thln-wp.css', array( 'thln' ), THLN_VERSION );
	wp_enqueue_script( 'thln', THLN_URI . '/assets/js/thln.js', array(), THLN_VERSION, array( 'strategy' => 'defer', 'in_footer' => true ) );
}

// Preload the self-hosted font so headings don't flash in a fallback face.
add_action( 'wp_head', 'thln_preload_font', 1 );
function thln_preload_font() {
	printf(
		'<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>' . "\n",
		esc_url( THLN_URI . '/assets/fonts/manrope-latin-var.woff2' )
	);
}

// Button and group styles Holly can pick from the block sidebar.
add_action( 'init', 'thln_block_styles' );
function thln_block_styles() {
	register_block_style( 'core/button', array( 'name' => 'thln-light', 'label' => __( 'Light purple', 'thln' ) ) );
	register_block_style( 'core/button', array( 'name' => 'thln-text-link', 'label' => __( 'Text link', 'thln' ) ) );
	register_block_style( 'core/paragraph', array( 'name' => 'thln-eyebrow', 'label' => __( 'Eyebrow', 'thln' ) ) );
	register_block_style( 'core/paragraph', array( 'name' => 'thln-microcopy', 'label' => __( 'Small print', 'thln' ) ) );
	register_block_style( 'core/quote', array( 'name' => 'thln-pull', 'label' => __( 'Pull quote', 'thln' ) ) );
}

add_action( 'init', 'thln_pattern_categories' );
function thln_pattern_categories() {
	register_block_pattern_category( 'thln-pages', array( 'label' => __( 'THLN: Full pages', 'thln' ) ) );
	register_block_pattern_category( 'thln-sections', array( 'label' => __( 'THLN: Sections', 'thln' ) ) );
}

/**
 * Pattern images live in the theme. Patterns reference them with this helper
 * so the URLs are right on any domain.
 */
function thln_img( $file ) {
	return esc_url( THLN_URI . '/assets/img/' . $file );
}

/**
 * The DEEP ROOTS Navigator link lives in one place (Appearance › Customize ›
 * THLN Site Settings). Any button or link pointing to "#roadmap" is sent there.
 */
function thln_navigator_url() {
	return esc_url( get_theme_mod( 'thln_navigator_url', 'https://navigator.thehairlossnutritionist.com' ) );
}

add_filter( 'render_block', 'thln_replace_roadmap_links', 10, 1 );
function thln_replace_roadmap_links( $html ) {
	if ( false === strpos( $html, '#roadmap' ) ) {
		return $html;
	}
	return str_replace( array( 'href="#roadmap"', "href='#roadmap'" ), 'href="' . thln_navigator_url() . '"', $html );
}

add_filter( 'nav_menu_link_attributes', 'thln_menu_roadmap_links' );
function thln_menu_roadmap_links( $atts ) {
	if ( isset( $atts['href'] ) && '#roadmap' === $atts['href'] ) {
		$atts['href'] = thln_navigator_url();
	}
	return $atts;
}
