<?php
/**
 * Header and footer.
 *
 * Replaces Astra's header/footer builder output with the THLN header and
 * footer. Content stays editable: logo (Site Identity), menus (Appearance ›
 * Menus), button text, Navigator link and tagline (THLN Site Settings).
 */

defined( 'ABSPATH' ) || exit;

add_action( 'wp', 'thln_swap_header_footer', 99 );
function thln_swap_header_footer() {
	remove_all_actions( 'astra_header' );
	remove_all_actions( 'astra_footer' );
	add_action( 'astra_header', 'thln_header' );
	add_action( 'astra_footer', 'thln_footer' );
}

/**
 * Link to a page by its path, falling back to a plain path when the page
 * doesn't exist yet. Used only when no menu has been assigned.
 */
function thln_page_link( $path ) {
	$page = get_page_by_path( $path );
	return $page ? get_permalink( $page ) : home_url( '/' . $path . '/' );
}

function thln_fallback_items( $items ) {
	$out = '';
	foreach ( $items as $label => $url ) {
		$current = ( untrailingslashit( $url ) === untrailingslashit( home_url( add_query_arg( array() ) ) ) ) ? ' aria-current="page"' : '';
		$out    .= sprintf( '<li><a href="%s"%s>%s</a></li>', esc_url( $url ), $current, esc_html( $label ) );
	}
	return $out;
}

function thln_logo() {
	if ( has_custom_logo() ) {
		$id  = get_theme_mod( 'custom_logo' );
		$img = wp_get_attachment_image( $id, 'full', false, array( 'alt' => get_bloginfo( 'name' ), 'loading' => false ) );
	} else {
		$img = sprintf( '<img src="%s" alt="%s" width="900" height="389">', thln_img( 'logo.webp' ), esc_attr( get_bloginfo( 'name' ) ) );
	}
	return $img;
}

function thln_header() {
	$button = get_theme_mod( 'thln_header_button', 'Get My Hair Roadmap' );
	?>
	<header class="thln-header">
		<div class="container thln-header__inner">
			<a class="thln-logo" href="<?php echo esc_url( home_url( '/' ) ); ?>" aria-label="<?php echo esc_attr( get_bloginfo( 'name' ) . ' — home' ); ?>"><?php echo thln_logo(); // phpcs:ignore WordPress.Security.EscapeOutput ?></a>
			<nav class="thln-nav" id="primary-nav" aria-label="<?php esc_attr_e( 'Primary', 'thln' ); ?>">
				<?php
				if ( has_nav_menu( 'primary' ) ) {
					wp_nav_menu(
						array(
							'theme_location' => 'primary',
							'container'      => false,
							'menu_class'     => '',
							'items_wrap'     => '<ul>%3$s</ul>',
							'depth'          => 1,
							'fallback_cb'    => false,
						)
					);
				} else {
					echo '<ul>' . thln_fallback_items( // phpcs:ignore WordPress.Security.EscapeOutput
						array(
							__( 'Home', 'thln' )      => home_url( '/' ),
							__( 'About', 'thln' )     => thln_page_link( 'about' ),
							__( 'Blog', 'thln' )      => thln_page_link( 'blog' ),
							__( 'Resources', 'thln' ) => thln_page_link( 'shop' ),
							__( 'Contact', 'thln' )   => thln_page_link( 'contact' ),
						)
					) . '</ul>';
				}
				?>
			</nav>
			<?php if ( $button ) : ?>
				<div class="header-cta">
					<a class="btn btn--sm" href="<?php echo thln_navigator_url(); // phpcs:ignore ?>"><?php echo esc_html( $button ); ?></a>
				</div>
			<?php endif; ?>
			<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="<?php esc_attr_e( 'Open menu', 'thln' ); ?>">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg>
			</button>
		</div>
	</header>
	<?php
}

function thln_footer_menu( $location, $fallback ) {
	if ( has_nav_menu( $location ) ) {
		wp_nav_menu(
			array(
				'theme_location' => $location,
				'container'      => false,
				'menu_class'     => '',
				'items_wrap'     => '<ul>%3$s</ul>',
				'depth'          => 1,
				'fallback_cb'    => false,
			)
		);
		return;
	}
	echo '<ul>' . thln_fallback_items( $fallback ) . '</ul>'; // phpcs:ignore WordPress.Security.EscapeOutput
}

function thln_footer() {
	$tagline    = get_theme_mod( 'thln_footer_tagline', 'Helping women make sense of their hair loss and take action where they can.' );
	$disclaimer = get_theme_mod( 'thln_footer_disclaimer', '' );
	$privacy    = get_privacy_policy_url();
	?>
	<footer class="thln-footer">
		<div class="container">
			<div class="thln-footer__top">
				<div class="thln-footer__brand">
					<?php echo thln_logo(); // phpcs:ignore ?>
					<?php if ( $tagline ) : ?>
						<p><?php echo esc_html( $tagline ); ?></p>
					<?php endif; ?>
				</div>
				<nav aria-label="<?php esc_attr_e( 'Footer', 'thln' ); ?>">
					<h2><?php esc_html_e( 'Explore', 'thln' ); ?></h2>
					<?php
					thln_footer_menu(
						'thln-footer-explore',
						array(
							__( 'About', 'thln' )                => thln_page_link( 'about' ),
							__( 'Blog', 'thln' )                 => thln_page_link( 'blog' ),
							__( 'Resources', 'thln' )            => thln_page_link( 'shop' ),
							__( 'DEEP ROOTS Navigator', 'thln' ) => thln_navigator_url(),
						)
					);
					?>
				</nav>
				<nav aria-label="<?php esc_attr_e( 'Legal', 'thln' ); ?>">
					<h2><?php esc_html_e( 'The fine print', 'thln' ); ?></h2>
					<?php
					thln_footer_menu(
						'thln-footer-legal',
						array(
							__( 'Privacy Policy', 'thln' ) => $privacy ? $privacy : thln_page_link( 'privacy-policy' ),
							__( 'Terms', 'thln' )          => thln_page_link( 'terms' ),
							__( 'Disclaimer', 'thln' )     => thln_page_link( 'disclaimer' ),
							__( 'Contact', 'thln' )        => thln_page_link( 'contact' ),
						)
					);
					?>
				</nav>
			</div>
			<div class="thln-footer__bottom">
				<p>&copy; <?php echo esc_html( gmdate( 'Y' ) . ' ' . get_bloginfo( 'name' ) ); ?></p>
			</div>
			<?php if ( $disclaimer ) : ?>
				<p class="thln-footer__disclaimer"><?php echo esc_html( $disclaimer ); ?></p>
			<?php endif; ?>
		</div>
	</footer>
	<?php
}
