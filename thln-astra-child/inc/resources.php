<?php
/**
 * Resources: a simple content type for the tools, downloads and guides shown
 * on the Resources (/shop/) page.
 *
 * Holly adds or edits a resource under Resources in the admin menu. The page
 * places them with shortcodes ([thln_resources section="tools"] etc.), so new
 * resources appear without editing the page or the theme.
 */

defined( 'ABSPATH' ) || exit;

const THLN_RES_SECTIONS = array(
	'guides'    => 'Guides & paid resources',
	'tools'     => 'Free tools',
	'downloads' => 'Free downloads',
);

/* --------------------------------------------------------------- Post type */

add_action( 'init', 'thln_register_resource_type' );
function thln_register_resource_type() {
	register_post_type(
		'thln_resource',
		array(
			'labels'          => array(
				'name'               => __( 'Resources', 'thln' ),
				'singular_name'      => __( 'Resource', 'thln' ),
				'add_new'            => __( 'Add resource', 'thln' ),
				'add_new_item'       => __( 'Add resource', 'thln' ),
				'edit_item'          => __( 'Edit resource', 'thln' ),
				'all_items'          => __( 'All resources', 'thln' ),
				'search_items'       => __( 'Search resources', 'thln' ),
				'not_found'          => __( 'No resources yet.', 'thln' ),
				'featured_image'     => __( 'Card image', 'thln' ),
				'set_featured_image' => __( 'Set card image', 'thln' ),
			),
			'public'          => false,
			'show_ui'         => true,
			'show_in_menu'    => true,
			'menu_position'   => 21,
			'menu_icon'       => 'dashicons-portfolio',
			'supports'        => array( 'title', 'thumbnail', 'page-attributes' ),
			'capability_type' => 'post',
			'show_in_rest'    => false,
		)
	);
}

function thln_resource_fields() {
	return array(
		'section'      => array( 'label' => __( 'Section on the Resources page', 'thln' ), 'type' => 'select', 'options' => array( 'guides' => 'Guides & paid resources', 'tools' => 'Free tools', 'downloads' => 'Free downloads' ) ),
		'access'       => array( 'label' => __( 'Free or paid', 'thln' ), 'type' => 'select', 'options' => array( 'free' => 'Free', 'paid' => 'Paid' ) ),
		'type_label'   => array( 'label' => __( 'Type label', 'thln' ), 'type' => 'text', 'help' => __( 'Short word shown next to the Free/Paid badge, e.g. Quiz, Screening tool, PDF guide, Guide.', 'thln' ) ),
		'lede'         => array( 'label' => __( 'Bold first line (optional)', 'thln' ), 'type' => 'text' ),
		'description'  => array( 'label' => __( 'Short description', 'thln' ), 'type' => 'textarea' ),
		'points'       => array( 'label' => __( 'Bullet points (optional)', 'thln' ), 'type' => 'textarea', 'help' => __( 'One per line. Shown with ✦ markers.', 'thln' ) ),
		'button_label' => array( 'label' => __( 'Button text', 'thln' ), 'type' => 'text', 'help' => __( 'e.g. Take the quiz, Send me the guide, Get the guide — $19', 'thln' ) ),
		'url'          => array( 'label' => __( 'Button link', 'thln' ), 'type' => 'url' ),
		'new_tab'      => array( 'label' => __( 'Open the link in a new tab', 'thln' ), 'type' => 'checkbox' ),
		'fine_print'   => array( 'label' => __( 'Small print under the button (optional)', 'thln' ), 'type' => 'textarea' ),
	);
}

function thln_res_meta( $post_id, $key ) {
	return get_post_meta( $post_id, '_thln_' . $key, true );
}

/* --------------------------------------------------------------- Edit screen */

add_action( 'add_meta_boxes_thln_resource', 'thln_resource_meta_box' );
function thln_resource_meta_box() {
	add_meta_box( 'thln_resource_details', __( 'Resource details', 'thln' ), 'thln_resource_meta_box_html', 'thln_resource', 'normal', 'high' );
}

function thln_resource_meta_box_html( $post ) {
	wp_nonce_field( 'thln_resource_save', 'thln_resource_nonce' );
	echo '<p style="margin-top:0">' . esc_html__( 'The title above is the card heading. Set the card image in the "Card image" box. Use "Order" (Page Attributes) to sort cards within a section: lower numbers come first.', 'thln' ) . '</p>';
	echo '<table class="form-table" role="presentation"><tbody>';
	foreach ( thln_resource_fields() as $key => $f ) {
		$id    = 'thln_' . $key;
		$value = thln_res_meta( $post->ID, $key );
		echo '<tr><th scope="row"><label for="' . esc_attr( $id ) . '">' . esc_html( $f['label'] ) . '</label></th><td>';
		switch ( $f['type'] ) {
			case 'select':
				echo '<select id="' . esc_attr( $id ) . '" name="' . esc_attr( $id ) . '">';
				foreach ( $f['options'] as $ov => $ol ) {
					echo '<option value="' . esc_attr( $ov ) . '"' . selected( $value, $ov, false ) . '>' . esc_html( $ol ) . '</option>';
				}
				echo '</select>';
				break;
			case 'textarea':
				echo '<textarea class="large-text" rows="3" id="' . esc_attr( $id ) . '" name="' . esc_attr( $id ) . '">' . esc_textarea( $value ) . '</textarea>';
				break;
			case 'checkbox':
				echo '<input type="checkbox" id="' . esc_attr( $id ) . '" name="' . esc_attr( $id ) . '" value="1"' . checked( $value, '1', false ) . '>';
				break;
			default:
				echo '<input class="regular-text" type="' . esc_attr( $f['type'] ) . '" id="' . esc_attr( $id ) . '" name="' . esc_attr( $id ) . '" value="' . esc_attr( $value ) . '">';
		}
		if ( ! empty( $f['help'] ) ) {
			echo '<p class="description">' . esc_html( $f['help'] ) . '</p>';
		}
		echo '</td></tr>';
	}
	echo '</tbody></table>';
}

add_action( 'save_post_thln_resource', 'thln_resource_save' );
function thln_resource_save( $post_id ) {
	if ( ! isset( $_POST['thln_resource_nonce'] ) || ! wp_verify_nonce( sanitize_key( $_POST['thln_resource_nonce'] ), 'thln_resource_save' ) ) {
		return;
	}
	if ( ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) || ! current_user_can( 'edit_post', $post_id ) ) {
		return;
	}
	foreach ( thln_resource_fields() as $key => $f ) {
		$name = 'thln_' . $key;
		$raw  = isset( $_POST[ $name ] ) ? wp_unslash( $_POST[ $name ] ) : ''; // phpcs:ignore WordPress.Security.ValidatedSanitizedInput
		switch ( $f['type'] ) {
			case 'url':
				$val = esc_url_raw( $raw );
				break;
			case 'textarea':
				$val = sanitize_textarea_field( $raw );
				break;
			case 'checkbox':
				$val = $raw ? '1' : '';
				break;
			case 'select':
				$val = array_key_exists( $raw, $f['options'] ) ? $raw : '';
				break;
			default:
				$val = sanitize_text_field( $raw );
		}
		update_post_meta( $post_id, '_thln_' . $key, $val );
	}
}

/* Admin list columns */
add_filter( 'manage_thln_resource_posts_columns', 'thln_resource_columns' );
function thln_resource_columns( $cols ) {
	$new = array();
	foreach ( $cols as $k => $v ) {
		$new[ $k ] = $v;
		if ( 'title' === $k ) {
			$new['thln_section'] = __( 'Section', 'thln' );
			$new['thln_access']  = __( 'Free / Paid', 'thln' );
			$new['thln_order']   = __( 'Order', 'thln' );
		}
	}
	unset( $new['date'] );
	return $new;
}

add_action( 'manage_thln_resource_posts_custom_column', 'thln_resource_column_values', 10, 2 );
function thln_resource_column_values( $col, $post_id ) {
	if ( 'thln_section' === $col ) {
		$s = thln_res_meta( $post_id, 'section' );
		echo esc_html( isset( THLN_RES_SECTIONS[ $s ] ) ? THLN_RES_SECTIONS[ $s ] : '—' );
	} elseif ( 'thln_access' === $col ) {
		echo esc_html( 'paid' === thln_res_meta( $post_id, 'access' ) ? 'Paid' : 'Free' );
	} elseif ( 'thln_order' === $col ) {
		echo (int) get_post_field( 'menu_order', $post_id );
	}
}

add_action( 'pre_get_posts', 'thln_resource_admin_order' );
function thln_resource_admin_order( $q ) {
	if ( is_admin() && $q->is_main_query() && 'thln_resource' === $q->get( 'post_type' ) && ! $q->get( 'orderby' ) ) {
		$q->set( 'orderby', array( 'menu_order' => 'ASC', 'title' => 'ASC' ) );
	}
}

/* --------------------------------------------------------------- Front end */

function thln_get_resources( $section ) {
	return get_posts(
		array(
			'post_type'      => 'thln_resource',
			'post_status'    => 'publish',
			'posts_per_page' => -1,
			'meta_key'       => '_thln_section', // phpcs:ignore WordPress.DB.SlowDBQuery
			'meta_value'     => $section, // phpcs:ignore WordPress.DB.SlowDBQuery
			'orderby'        => array( 'menu_order' => 'ASC', 'title' => 'ASC' ),
		)
	);
}

function thln_res_badges( $id ) {
	$paid  = 'paid' === thln_res_meta( $id, 'access' );
	$label = thln_res_meta( $id, 'type_label' );
	$out   = '<span class="res-tool__meta"><span class="badge ' . ( $paid ? 'badge--paid' : 'badge--free' ) . '">' . ( $paid ? esc_html__( 'Paid', 'thln' ) : esc_html__( 'Free', 'thln' ) ) . '</span>';
	if ( $label ) {
		$out .= '<span class="badge badge--type">' . esc_html( $label ) . '</span>';
	}
	return $out . '</span>';
}

function thln_res_points( $id ) {
	$lines = array_filter( array_map( 'trim', explode( "\n", (string) thln_res_meta( $id, 'points' ) ) ) );
	if ( ! $lines ) {
		return '';
	}
	return '<ul class="res-points">' . implode( '', array_map( fn( $l ) => '<li>' . esc_html( $l ) . '</li>', $lines ) ) . '</ul>';
}

function thln_res_text( $id, $key, $tag = 'p', $cls = '' ) {
	$v = thln_res_meta( $id, $key );
	if ( '' === (string) $v ) {
		return '';
	}
	return sprintf( '<%1$s%2$s>%3$s</%1$s>', $tag, $cls ? ' class="' . esc_attr( $cls ) . '"' : '', nl2br( esc_html( $v ) ) );
}

function thln_res_link_attrs( $id ) {
	$url = thln_res_meta( $id, 'url' );
	$a   = ' href="' . esc_url( $url ? $url : '#' ) . '"';
	if ( thln_res_meta( $id, 'new_tab' ) ) {
		$a .= ' target="_blank" rel="noopener"';
	}
	return $a;
}

function thln_res_new_tab_note( $id ) {
	return thln_res_meta( $id, 'new_tab' ) ? '<span class="visually-hidden"> ' . esc_html__( '(opens in a new tab)', 'thln' ) . '</span>' : '';
}

function thln_render_tool( $r ) {
	$id    = $r->ID;
	$img   = has_post_thumbnail( $id ) ? get_the_post_thumbnail( $id, 'medium', array( 'alt' => '' ) ) : '';
	$label = thln_res_meta( $id, 'button_label' );
	return '<li><a class="res-tool"' . thln_res_link_attrs( $id ) . '>'
		. '<span class="res-tool__icon' . ( $img ? ' has-image' : '' ) . '">' . $img . '</span>'
		. '<div>' . thln_res_badges( $id )
		. '<h3>' . esc_html( get_the_title( $r ) ) . '</h3>'
		. thln_res_text( $id, 'description' )
		. ( $label ? '<span class="go">' . esc_html( $label ) . ' <span class="arrow" aria-hidden="true">→</span></span>' : '' )
		. thln_res_new_tab_note( $id )
		. thln_res_text( $id, 'fine_print', 'span', 'res-fine' )
		. '</div></a></li>';
}

function thln_render_download( $r ) {
	$id     = $r->ID;
	$img    = has_post_thumbnail( $id ) ? get_the_post_thumbnail( $id, 'large', array( 'alt' => '' ) ) : '<span class="sheet"><img src="' . thln_img( 'dr-01.webp' ) . '" alt=""></span>';
	$label  = thln_res_meta( $id, 'button_label' );
	$icon   = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg>';
	return '<li><div class="res-download">'
		. '<div class="res-download__visual' . ( has_post_thumbnail( $id ) ? ' has-image' : '' ) . '">' . $img . '</div>'
		. '<div class="res-download__body">' . thln_res_badges( $id )
		. '<h3>' . esc_html( get_the_title( $r ) ) . '</h3>'
		. thln_res_text( $id, 'lede', 'p', 'res-lede' )
		. thln_res_text( $id, 'description' )
		. thln_res_points( $id )
		. ( $label ? '<a class="btn btn--outline btn--sm"' . thln_res_link_attrs( $id ) . '>' . $icon . ' ' . esc_html( $label ) . thln_res_new_tab_note( $id ) . '</a>' : '' )
		. thln_res_text( $id, 'fine_print', 'p', 'res-fine' )
		. '</div></div></li>';
}

function thln_render_guide( $r ) {
	$id    = $r->ID;
	$title = get_the_title( $r );
	$cover = has_post_thumbnail( $id )
		? get_the_post_thumbnail( $id, 'large', array( 'alt' => '' ) )
		: '<div class="book" aria-hidden="true"><small>' . esc_html( get_bloginfo( 'name' ) ) . '</small><b>' . esc_html( $title ) . '</b><img src="' . thln_img( 'roots-02.webp' ) . '" alt=""></div>';
	$label = thln_res_meta( $id, 'button_label' );
	return '<li><article class="res-guide">'
		. '<div class="res-guide__cover' . ( has_post_thumbnail( $id ) ? ' has-image' : '' ) . '">' . $cover . '</div>'
		. '<div class="res-guide__body">' . thln_res_badges( $id )
		. '<h3>' . esc_html( $title ) . '</h3>'
		. thln_res_text( $id, 'lede', 'p', 'res-lede' )
		. thln_res_text( $id, 'description' )
		. thln_res_points( $id )
		. ( $label ? '<div class="res-guide__foot"><a class="btn"' . thln_res_link_attrs( $id ) . '>' . esc_html( $label ) . ' <span class="arrow" aria-hidden="true">→</span>' . thln_res_new_tab_note( $id ) . '</a></div>' : '' )
		. thln_res_text( $id, 'fine_print', 'p', 'res-fine' )
		. '</div></article></li>';
}

add_shortcode( 'thln_resources', 'thln_resources_shortcode' );
function thln_resources_shortcode( $atts ) {
	$atts    = shortcode_atts( array( 'section' => 'tools' ), $atts, 'thln_resources' );
	$section = sanitize_key( $atts['section'] );
	$items   = thln_get_resources( $section );
	if ( ! $items ) {
		return current_user_can( 'edit_posts' )
			? '<p class="proto-note">' . esc_html__( 'No resources in this section yet. Add one under Resources in the admin menu. (Only logged-in editors see this note.)', 'thln' ) . '</p>'
			: '';
	}
	$render = array( 'guides' => 'thln_render_guide', 'downloads' => 'thln_render_download' );
	$fn     = isset( $render[ $section ] ) ? $render[ $section ] : 'thln_render_tool';
	$cls    = 'guides' === $section ? 'res-grid res-grid--guides' : 'res-grid';
	return '<ul class="' . esc_attr( $cls ) . '">' . implode( '', array_map( $fn, $items ) ) . '</ul>';
}

/* Jump links under the Resources hero: only sections that have resources. */
add_shortcode( 'thln_resource_links', 'thln_resource_links_shortcode' );
function thln_resource_links_shortcode() {
	$links = array(
		'guides'    => array( 'paid', __( 'Paid', 'thln' ), __( 'Guides', 'thln' ) ),
		'tools'     => array( 'free', __( 'Free', 'thln' ), __( 'Tools', 'thln' ) ),
		'downloads' => array( 'free', __( 'Free', 'thln' ), __( 'Downloads', 'thln' ) ),
	);
	$out = '';
	foreach ( $links as $section => $l ) {
		if ( thln_get_resources( $section ) ) {
			$out .= sprintf( '<li><a href="#%s"><span class="badge badge--%s">%s</span> %s</a></li>', esc_attr( $section ), esc_attr( $l[0] ), esc_html( $l[1] ), esc_html( $l[2] ) );
		}
	}
	return $out ? '<ul class="res-key" aria-label="' . esc_attr__( 'Jump to a section', 'thln' ) . '">' . $out . '</ul>' : '';
}

/* ------------------------------------------------------- Starter resources */

add_action( 'admin_notices', 'thln_starter_notice' );
function thln_starter_notice() {
	$screen = get_current_screen();
	if ( ! $screen || 'edit-thln_resource' !== $screen->id || ! current_user_can( 'edit_posts' ) ) {
		return;
	}
	$count = wp_count_posts( 'thln_resource' );
	if ( (int) $count->publish + (int) $count->draft > 0 ) {
		return;
	}
	$url = wp_nonce_url( admin_url( 'admin-post.php?action=thln_add_starter_resources' ), 'thln_starter' );
	echo '<div class="notice notice-info"><p><strong>' . esc_html__( 'Start with your current resources?', 'thln' ) . '</strong> '
		. esc_html__( 'This adds the Hair Growth Grocery Guide, both iron tools and the 10 Nutrients guide with their copy and links. You can edit or delete them afterwards.', 'thln' )
		. '</p><p><a class="button button-primary" href="' . esc_url( $url ) . '">' . esc_html__( 'Add starter resources', 'thln' ) . '</a></p></div>';
}

add_action( 'admin_post_thln_add_starter_resources', 'thln_add_starter_resources' );
function thln_add_starter_resources() {
	check_admin_referer( 'thln_starter' );
	if ( ! current_user_can( 'edit_posts' ) ) {
		wp_die( esc_html__( 'Sorry, you are not allowed to do that.', 'thln' ) );
	}
	thln_create_starter_resources();
	wp_safe_redirect( admin_url( 'edit.php?post_type=thln_resource' ) );
	exit;
}

function thln_create_starter_resources() {
	$items = array(
		array(
			'title' => 'Hair Growth Grocery Guide', 'order' => 1, 'section' => 'guides', 'access' => 'paid', 'type_label' => 'Guide',
			'lede' => 'Stop guessing what to eat for hair growth.',
			'description' => "Here's a beginner-friendly nutrition guide for women experiencing hair loss. Skip the conflicting advice and learn how to grocery shop with more confidence, clarity, and intention.",
			'points' => "Learn which nutrients support healthy hair\nDiscover everyday foods that provide those nutrients\nBuild balanced, hair-supportive meals without restrictive dieting\nStop wasting money on random supplements and products",
			'button_label' => 'Get the guide — $19', 'url' => 'https://thehairlossnutritionist.com/hair-growth-grocery-guide/',
			'fine_print' => 'Instant digital download. Practical nutrition guidance from a Registered Dietitian.',
		),
		array(
			'title' => 'Could Low Iron Be Contributing to Your Hair Loss?', 'order' => 1, 'section' => 'tools', 'access' => 'free', 'type_label' => 'Screening tool',
			'description' => 'Answer a few quick questions to see whether low iron could be contributing to your hair loss—and what your next best step might be.',
			'button_label' => 'Start the screening', 'url' => 'https://thehairlossnutritionist.com/do-you-need-iron-for-hair-loss/', 'image' => 'iron-screening-icon.webp',
		),
		array(
			'title' => 'Which Iron Supplement Is Right for You?', 'order' => 2, 'section' => 'tools', 'access' => 'free', 'type_label' => 'Quiz',
			'description' => 'Answer a few quick questions to discover which iron supplements may be the best fit for your needs and preferences.',
			'button_label' => 'Take the quiz', 'url' => 'https://thehairlossnutritionist.com/iron-supplement-quiz/', 'image' => 'iron-supplement-quiz-icon.webp',
		),
		array(
			'title' => 'Healthy hair starts from within.', 'order' => 1, 'section' => 'downloads', 'access' => 'free', 'type_label' => 'PDF guide',
			'description' => 'A free, beginner-friendly guide to help you understand the 10 nutrients commonly linked to healthy hair. No complicated science. No restrictive diets. Just a simple place to start.',
			'points' => "Learn about 10 nutrients that support healthy hair.\nDiscover everyday foods that naturally provide them.\nBuild a stronger foundation before spending money on products",
			'button_label' => 'Send me the guide', 'url' => 'https://thehairlossnutritionist.com/10-nutrients/',
		),
	);

	require_once ABSPATH . 'wp-admin/includes/image.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/media.php';

	foreach ( $items as $it ) {
		$id = wp_insert_post(
			array(
				'post_type'   => 'thln_resource',
				'post_status' => 'publish',
				'post_title'  => $it['title'],
				'menu_order'  => $it['order'],
			)
		);
		if ( ! $id || is_wp_error( $id ) ) {
			continue;
		}
		foreach ( array_keys( thln_resource_fields() ) as $key ) {
			if ( isset( $it[ $key ] ) ) {
				update_post_meta( $id, '_thln_' . $key, $it[ $key ] );
			}
		}
		if ( ! empty( $it['image'] ) ) {
			$tmp = wp_tempnam( $it['image'] );
			if ( $tmp && copy( THLN_DIR . '/assets/img/' . $it['image'], $tmp ) ) {
				$att = media_handle_sideload( array( 'name' => $it['image'], 'tmp_name' => $tmp ), $id, $it['title'] );
				if ( ! is_wp_error( $att ) ) {
					set_post_thumbnail( $id, $att );
				} else {
					wp_delete_file( $tmp );
				}
			}
		}
	}
}
