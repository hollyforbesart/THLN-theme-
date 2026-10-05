<?php
/**
 * THLN Astra Child — theme bootstrap.
 *
 * The theme controls look and behavior. Everything Holly edits day to day
 * (page copy, images, buttons, menus, resources) stays in WordPress.
 */

defined( 'ABSPATH' ) || exit;

define( 'THLN_VERSION', '1.0.0' );
define( 'THLN_DIR', get_stylesheet_directory() );
define( 'THLN_URI', get_stylesheet_directory_uri() );

require THLN_DIR . '/inc/setup.php';
require THLN_DIR . '/inc/customizer.php';
require THLN_DIR . '/inc/layout.php';
require THLN_DIR . '/inc/header-footer.php';
require THLN_DIR . '/inc/resources.php';
