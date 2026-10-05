<?php
/**
 * Appearance › Customize › THLN Site Settings.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'customize_register', 'thln_customize_register' );
function thln_customize_register( $wp_customize ) {
	$wp_customize->add_section(
		'thln_site',
		array(
			'title'       => __( 'THLN Site Settings', 'thln' ),
			'description' => __( 'Header button, Navigator link and footer text. Your logo is under Site Identity; menus are under Menus.', 'thln' ),
			'priority'    => 25,
		)
	);

	$fields = array(
		'thln_navigator_url'   => array(
			'label'       => __( 'DEEP ROOTS Navigator link', 'thln' ),
			'description' => __( 'Every "Get My Hair Roadmap" button uses this link. In page content, link a button to #roadmap to use it.', 'thln' ),
			'default'     => 'https://navigator.thehairlossnutritionist.com',
			'type'        => 'url',
			'sanitize'    => 'esc_url_raw',
		),
		'thln_header_button'   => array(
			'label'    => __( 'Header button text', 'thln' ),
			'default'  => 'Get My Hair Roadmap',
			'type'     => 'text',
			'sanitize' => 'sanitize_text_field',
		),
		'thln_footer_tagline'  => array(
			'label'    => __( 'Footer tagline', 'thln' ),
			'default'  => 'Helping women make sense of their hair loss and take action where they can.',
			'type'     => 'textarea',
			'sanitize' => 'sanitize_textarea_field',
		),
		'thln_footer_disclaimer' => array(
			'label'       => __( 'Footer disclaimer (optional)', 'thln' ),
			'description' => __( 'A short line under the footer, for example a medical disclaimer. Leave empty to hide.', 'thln' ),
			'default'     => '',
			'type'        => 'textarea',
			'sanitize'    => 'sanitize_textarea_field',
		),
	);

	foreach ( $fields as $id => $f ) {
		$wp_customize->add_setting(
			$id,
			array(
				'default'           => $f['default'],
				'sanitize_callback' => $f['sanitize'],
				'transport'         => 'refresh',
			)
		);
		$wp_customize->add_control(
			$id,
			array(
				'label'       => $f['label'],
				'description' => isset( $f['description'] ) ? $f['description'] : '',
				'section'     => 'thln_site',
				'type'        => $f['type'],
			)
		);
	}
}
