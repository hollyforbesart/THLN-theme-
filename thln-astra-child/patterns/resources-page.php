<?php
/**
 * Title: Resources page (full page)
 * Slug: thln/resources-page
 * Categories: thln-pages
 * Description: Resources page. The cards come from Resources in the admin menu.
 * Block Types: core/post-content
 * Post Types: page
 * Viewport Width: 1400
 */
defined( 'ABSPATH' ) || exit;
?>
<?php include get_theme_file_path( 'parts/resources-hero.php' ); ?>
<?php include get_theme_file_path( 'parts/resources-guides.php' ); ?>
<?php include get_theme_file_path( 'parts/resources-navigator.php' ); ?>
<?php include get_theme_file_path( 'parts/resources-tools.php' ); ?>
<?php include get_theme_file_path( 'parts/resources-downloads.php' ); ?>
