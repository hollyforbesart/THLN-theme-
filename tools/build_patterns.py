"""Generate the THLN block patterns.

Run from the repo root:  python3 tools/build_patterns.py

Writes thln-astra-child/parts/*.php (one file per page section) and
thln-astra-child/patterns/*.php (what shows up in the WordPress inserter).
Full-page patterns include several parts, so each section's copy exists once.
Edit copy here, re-run, and re-zip the theme. Once a page is built in
WordPress, Holly edits the page itself; this file only seeds new pages.
"""

import os
from blocks import (group, p, h, img, button, buttons, lst, quote, shortcode,
                    section, container)

ROOT = os.path.join(os.path.dirname(__file__), "..", "thln-astra-child")
PARTS = os.path.join(ROOT, "parts")
PATTERNS = os.path.join(ROOT, "patterns")

MICRO = "Free • 20 questions • Personalized results"
CTA = "Get My Hair Roadmap"

# --------------------------------------------------------------------- HOME
home_hero = section([
    container([
        img("hero.webp", "A woman with curly hair looks down thoughtfully, running her fingers through her hair at her part.", "hero__media"),
        group([
            p("Hair loss is complicated.<br>Your next step doesn't have to be.", "eyebrow hero__eyebrow"),
            h("<strong>Stop guessing</strong><br>what your hair needs.", 1),
            group([
                p("Iron. Hormones. Stress. Your diet. Your medications. Your scalp. Your styling. Everything intertwines and contributes to your hair loss."),
                p("So I created a Navigator that helps you figure out what may deserve your attention, and know what to do next."),
            ], "hero__body"),
            buttons(button(CTA)),
            p(MICRO, "microcopy"),
        ], "hero__content"),
    ], "hero__inner"),
], "hero")

home_problem = section([
    container([
        h('You\'ve probably already heard a hundred things you "should" be doing.', 2, "noise__head"),
        lst(["Take biotin.", "Check your iron.", "Eat more protein.", "Try minoxidil.", "Fix your hormones.",
             "Lower your stress.", "Buy this serum.", "Stop eating that."], "noise__list"),
        group([
            group([p("Some of it may matter for you."), p("Some of it may not.")], "noise__maybe"),
            group([
                p("You don't need more things to try."),
                p("You need to know what <em>actually deserves your attention.</em>", "noise__strong"),
                buttons(button("Show Me Where to Start", style="thln-text-link")),
            ], "noise__statement"),
        ], "noise__resolve"),
    ]),
], "section bg-plum on-plum noise")

DR = [("dr-01.webp", "Diet &amp; Deficiencies"), ("dr-02.webp", "Endocrine Imbalances"),
      ("dr-03.webp", "Emotional &amp; Mental Stress"), ("dr-04.webp", "Physical Stress &amp; Illness"),
      ("dr-05.webp", "Reactions to Medications"), ("dr-06.webp", "Other Chronic Conditions"),
      ("dr-07.webp", "Overprocessing &amp; Tension"), ("dr-08.webp", "Triggers in Your History"),
      ("dr-09.webp", "Shared Family Patterns")]

home_deep_roots = section([
    container([
        group([
            p("Look at the bigger picture", "eyebrow eyebrow--rule"),
            h("There's more to hair loss than hair."),
            p('<strong>DEEP ROOTS</strong> helps you look at nine areas that may hold clues about what\'s happening with your hair.', "lead"),
            group([
                p("You don't have to sort through all of this by yourself.", "deep-roots__close"),
                buttons(button(CTA)),
            ], "deep-roots__cta"),
        ], "deep-roots__intro"),
        group([group([img(f), p(name, "dr-tile__label")], "dr-tile") for f, name in DR], "dr-map"),
    ], "deep-roots__grid"),
], "section bg-cream deep-roots")

ROOTS = [("roots-01.webp", "R", "Recognize the root cause"), ("roots-02.webp", "O", "Optimize nutrition &amp; lifestyle"),
         ("roots-03.webp", "O", "Optimize scalp"), ("roots-04.webp", "T", "Tame tension"), ("roots-05.webp", "S", "Soothe stress")]

home_roots = section([
    container([
        group([
            h("Okay, so what do you actually do?"),
            p("Follow my <strong>ROOTS</strong> framework for Recovery."),
        ], "roots__head"),
        group([group([img(f), p(letter, "roots-step__letter"), p(name, "roots-step__name")], "roots-step")
               for f, letter, name in ROOTS], "roots-track"),
        group([
            group([
                p("Not every step will look the same for every woman. And not everything will be something you can fix on your own."),
                p("But you must:", "must"),
            ], "roots__resolve-intro"),
            group([p("Understand what's going on."), p("Do what you can."), p("Get help with the rest.")], "mantra"),
        ], "roots__resolve"),
    ]),
], "section bg-lavender roots")

PATH = [("01", "See the bigger picture", "Look beyond your hair and see what else may be going on in your body."),
        ("02", "Know what needs your attention", "Focus on what actually matters for YOU."),
        ("03", "Take action where you can", "Do your part and work on the things that are within your control."),
        ("04", "Get help when you need it", "Bring in the professionals for the things you can't solve alone.")]

home_path = section([
    container([
        group([h("So here's a path forward."), img("hair-to-map.webp", "", "path__art")], "path__head"),
        group([group([p(n, "path-step__num"), h(t, 3), p(d)], "path-step") for n, t, d in PATH], "path-steps"),
        group([buttons(button(CTA)), p("Start with the free DEEP ROOTS Navigator.")], "path__cta"),
    ]),
], "section bg-sand path")

home_holly = section([
    container([
        img("holly.webp", "Holly, The Hair Loss Nutritionist", "holly-photo holly__media"),
        group([
            p("Hi, I'm Holly", "eyebrow eyebrow--rule"),
            h("I'm just a girl who lost her hair too."),
            p("My own hair-loss journey has taken me through doctor's appointments, bloodwork, a biopsy, treatments, supplements, nutrition changes and a whole lot of research. And somewhere along the way, I realized how easy it is to spend your time, money and energy trying things without ever feeling sure you're doing the right thing."),
            p("I happened to already be a Registered Dietitian when my hair started falling out, so nutrition was one piece of the puzzle I knew how to investigate. And even with having this background, there were some things I didn't know (like how important it is to have ferritin the optimal range, not just \"normal\")."),
            p("But hair loss has taught me something much bigger than nutrition:"),
            quote(["It's really just a revelation of what is happening in your body, and you cannot control everything that happens to your body. But there are some things you can and must take action on."], "is-style-thln-pull"),
            p("That's the philosophy behind The Hair Loss Nutritionist."),
            p("<strong>I don't have all the answers. I don't have a miracle cure.</strong> And I'm not going to tell you that every hair problem can be fixed with food or supplements.", "holly__honest"),
            p("What I can do is share what I know, help you make sense of the information in front of you, and give you tools to participate in your own recovery."),
            buttons(button("Read My Story", "/about/", "thln-text-link")),
        ], "holly__copy"),
    ], "holly"),
], "section bg-white")

home_final = section([
    container([
        group([
            h("Your hair is changing.<br><em>What are you going to do next?</em>"),
            group([
                p("You don't need another random product, supplement or list of things that might help."),
                p("Start by figuring out what deserves your attention."),
            ], "final-cta__body"),
        ]),
        group([
            p("Take the free DEEP ROOTS Navigator to look at your bigger picture and get personalized next steps.", "big"),
            buttons(button(CTA, style="thln-light")),
            p(MICRO, "microcopy"),
        ], "final-cta__action"),
    ], "final-cta__inner"),
], "section bg-plum on-plum final-cta")

# -------------------------------------------------------------------- ABOUT
def story(label_children, body_children, bg, cls=None):
    return section([container([group(label_children, "story-block__label"),
                               group(body_children, "story-block__body")], "story-block")],
                   f"section {bg}" + (f" {cls}" if cls else ""))

about_hero = section([
    container([
        group([
            p("About The Hair Loss Nutritionist", "eyebrow eyebrow--rule"),
            h("I'm just a girl who lost her hair too.", 1),
            p("And I'm still figuring it out.", "sub"),
            p("I'm Holly, a Registered Dietitian who has spent the last several years navigating my own hair loss via asking questions, trying treatments, changing course, learning more about my body and figuring out what to do next."),
            p("The Hair Loss Nutritionist grew out of that experience."),
            p("Not because I found the secret to growing your hair back.", "turn-lead"),
            p("Because I learned how important it is to participate in your own recovery.", "turn"),
        ], "about-hero__copy"),
        img("holly.webp", "Holly, The Hair Loss Nutritionist", "holly-photo"),
    ], "about-hero"),
], "section bg-cream page-top")

about_story = story(
    [p("My story", "eyebrow eyebrow--rule"), h("It started with a lot of hair in the shower <em>(sound familiar?)</em>")],
    [p("In 2021, my hair started shedding. A lot.", "beat"),
     p("At first I blamed the braids I'd been wearing. Then stress. I had recently started a difficult job and thought, <em>Wow. Am I really THAT stressed?</em>"),
     p("But the shedding continued and my already fine hair felt thinner."),
     p("And I had no idea what I was supposed to do about it."),
     p("I was already a Registered Dietitian. I understood nutrition, labs and the human body."),
     p("I still didn't understand my hair loss.", "beat"),
     p("So I started looking for answers.")], "bg-white")

about_question = story(
    [h("One answer led to another question.")],
    [p("I saw a trichologist. We talked about my diet, my hair-care practices and my labs."),
     group([p("11.9", "big-num__value"), p("My ferritin was 11.9. That was one clue.", "big-num__label")], "big-num"),
     p("I worked on my iron levels. I took supplements. I went for scalp treatments. Eventually, the excessive shedding stopped."),
     p("But my hair still didn't feel right.", "beat"),
     p("In 2022, I finally saw a dermatologist who told me:"),
     quote(['"We\'re not going to guess."'], "is-style-thln-pull"),
     p("Let's do a biopsy of your scalp and see what's going on there. I never even knew that was a thing. I only knew of biopsies in terms of looking for cancer. Not diagnosing alopecia."),
     p("I didn't even know there were multiple types of alopecia until I got a call saying my biopsy results were positive for CCCA which stands for central centrifugal cicatricial alopecia, a type of scarring hair loss I'd never even heard of."),
     p("I actually told him I didn't think I had it."),
     p("I had Googled CCCA, looked at the pictures and thought, <em>That's not what my hair looks like.</em>"),
     p("He explained that mine had been caught early."),
     p("That moment has stayed with me.", "beat"),
     p("I'm glad I kept asking questions. I'm glad I didn't wait. Because the dermatologist told me most folks wait too long and come to him when it's too late.")], "bg-cream")

about_quote = section([container([quote(["I'm glad I kept asking questions. I'm glad I didn't wait."])])],
                      "section section--tight bg-plum on-plum quote-band")

about_before_after = story(
    [h("The part that doesn't fit into a before &amp; after")],
    [p("I wish I could tell you that was the end of the story.<br>It wasn't.", "beat"),
     p("I've tried medications, injections, topical treatments, supplements, microneedling, scalp treatments, different hair-care practices and lifestyle changes (sometimes I like to try stuff in the name of science and see what happens)."),
     p("Some things helped.<br>Some things didn't.", "beat"),
     p("Eventually my hair grew thicker again."),
     p("And then there were more questions."),
     p("I visited a trichologist and I learned I had seborrheic dermatitis. Another professional raised the possibility of androgenetic alopecia. Life changed. I moved. I couldn't continue with the same providers."),
     p("So here I am, years later, still learning about my own hair."),
     p("I've stopped expecting hair loss to be something I solve once and never think about again."),
     p("For me, it has meant paying attention. Following up. Documenting. Asking better questions. Changing course when I need to."),
     p("And continuing to do something.", "beat")], "bg-white")

about_believe = story(
    [p("What I believe", "eyebrow eyebrow--rule"),
     h("You can't control everything that happens to your body."),
     p("But there are things you can do.", "beat")],
    [p("That's probably the biggest thing hair loss has taught me."),
     p("Your hair can tell you that something is happening. Maybe it's your nutrition. Maybe it's your hormones. Maybe it's illness, stress, medication, your scalp, your styling practices, etc."),
     p("Sometimes it's several things at once."),
     p("You may not be able to fix every one of them yourself."),
     lst(["But you can pay attention.", "You can ask questions.", "You can nourish your body.", "You can follow your treatment.",
          "You can stop doing things that are hurting your hair.", "You can track what's changing.", "You can get another opinion.",
          "You can go back when something still isn't right.", "You can participate in your own recovery."], "can-list", ordered=True),
     p("<strong>That's what I want The Hair Loss Nutritionist to help you do.</strong>")], "bg-lavender")

about_why = section([
    container([
        group([
            group([p("Why The Hair Loss Nutritionist exists", "eyebrow eyebrow--rule"), h("Less guessing. More doing.")], "story-block__label"),
            group([
                p("There's no shortage of hair-loss advice."),
                p("Take this supplement. Buy this serum. Eat this food. Avoid that food. Get these labs. Try this treatment.", "muted-strong"),
                p("The problem is figuring out what actually matters for you.", "beat"),
                p("The Hair Loss Nutritionist exists to help women make sense of the nutrition, health, lifestyle and hair-loss information coming at them and turn that information into something useful."),
                p("Here you'll find evidence-based education, practical resources and tools designed to help you:"),
            ], "story-block__body"),
        ], "story-block"),
        lst(["understand the bigger picture behind your hair loss", "recognize what may deserve your attention",
             "work on the nutrition and lifestyle factors within your control", "ask better questions and navigate professional care",
             "track what you're doing long enough to know whether it's actually helping",
             "stop wasting money on random things just because someone online said they grow hair"], "split-list"),
        group([
            group([p("I don't believe every hair problem is nutritional."),
                   p("I don't believe every woman needs another supplement."),
                   p("And I definitely don't believe I have all the answers.")], "beliefs"),
            p("I believe in understanding what's going on, doing what you can, and getting help with the rest.", "belief-mantra"),
        ], "why__close"),
    ]),
], "section bg-cream")

about_nutrition = story(
    [h("Why nutrition is part of the conversation"), img("roots-02.webp", "", "story-icon")],
    [p("I happened to study nutrition before hair loss happened to me.", "beat"),
     p("I'm a Registered Dietitian with over 7 years of experience helping people understand how nutrition connects with health."),
     p("That background gave me a useful lens when I started dealing with my own hair loss but it also showed me how much I didn't know."),
     p("Hair loss pushed me to learn more about nutrient deficiencies, hair and scalp conditions, treatments, hormones, stress, styling practices and the many other pieces that can affect what happens on our heads."),
     p("I'm continuing that education today."),
     quote(["My role here isn't to replace your dermatologist, doctor or trichologist."], "is-style-thln-pull"),
     p("It's to help you understand the bigger picture, take action on the pieces you can influence, and recognize when something belongs in the hands of another professional.")], "bg-white")


def navigator_feature(eyebrow, title, paras, level=2):
    body = [p(eyebrow, "eyebrow"), h(title, level)]
    body += [p(x, "lead" if i == 0 else None) for i, x in enumerate(paras)]
    body += [buttons(button(CTA, style="thln-light")), p(MICRO, "microcopy")]
    return group([group(body, "navigator-feature__copy"),
                  img("navigator-illustration.webp", "", "navigator-feature__media")], "navigator-feature on-plum")


about_start = section([container([navigator_feature(
    "Start here", "Not sure what deserves your attention?",
    ["I built the DEEP ROOTS Navigator because I know what it's like to have ten possible explanations in your head and no idea where to start.",
     "Answer 20 questions about your health, nutrition, lifestyle and hair history and get personalized results to help you see the bigger picture and decide what to do next."])])],
    "section bg-cream")

about_talk = section([
    container([
        group([
            p("Talk to me", "eyebrow eyebrow--rule"),
            h("I want to know what you need."),
            p("The Hair Loss Nutritionist is still growing, and I don't want to build resources based only on what I think women with hair loss need."),
            p("If there's a question you can't seem to get answered, a resource you wish existed, or something about hair loss you want me to dig into, tell me."),
            p("And if you're a company, healthcare professional or organization interested in working together, I'd love to hear from you too."),
        ]),
        group([buttons(button("Contact Me", "/contact/", "outline")),
               p("Questions • Resource requests • Partnerships", "microcopy")]),
    ], "contact-band"),
], "section bg-sand")

# ------------------------------------------------------------------ CONTACT
navigator_band = section([container([group([
    img("navigator-illustration.webp", "", "nav-band__art"),
    group([h("Not sure what deserves your attention?"),
           p("Take the free DEEP ROOTS Navigator to look at your bigger picture and get personalized next steps.")]),
    buttons(button(CTA, style="thln-light")),
], "nav-band on-plum")])], "section section--tight bg-white")

contact_main = section([
    container([
        group([
            p("Talk to me", "eyebrow eyebrow--rule"),
            h("I want to know what you need.", 1),
            p("The Hair Loss Nutritionist is still growing, and I don't want to build resources based only on what I think women with hair loss need."),
            p("If there's a question you can't seem to get answered, a resource you wish existed, or something about hair loss you want me to dig into, tell me."),
            p("And if you're a company, healthcare professional or organization interested in working together, I'd love to hear from you too."),
            lst(["<strong>Questions</strong>", "<strong>Resource requests</strong>", "<strong>Partnerships</strong>"], "contact-reasons"),
        ], "contact-intro"),
        group([
            h("Send me a message", 2),
            p("Replace this paragraph with your WPForms form: click it, press the + button, search for WPForms and choose your contact form.", "form-placeholder"),
        ], "contact-form"),
    ], "contact-layout"),
], "section bg-cream page-top")

# ---------------------------------------------------------------- RESOURCES
res_hero = section([
    container([
        p("Resources", "eyebrow eyebrow--rule"),
        h("Tools and resources for your next step.", 1),
        p("Tools and resources to help you figure out what deserves your attention, and do something about it.", "lead"),
        shortcode("[thln_resource_links]"),
    ]),
], "page-hero bg-cream")


def res_section(anchor, title, intro, code, bg, extra=None):
    kids = [group([h(title), p(intro)], "res-section__head"), shortcode(code)]
    if extra:
        kids.append(extra)
    return section([container(kids)], f"res-section {bg}", anchor=anchor)


res_guides = res_section("guides", "Guides &amp; paid resources", "In-depth guides for when you're ready to take action on a specific area.",
                         '[thln_resources section="guides"]', "bg-white",
                         group([p("<strong>More guides are on the way.</strong>"),
                                p("New resources are built from what women with hair loss tell me they need."),
                                buttons(button("Tell me what you need", "/contact/", "thln-text-link"))], "res-soon"))

res_navigator = section([container([navigator_feature(
    "Start here · Free tool", "DEEP ROOTS Navigator",
    ["Hair loss is complicated. Your next step doesn't have to be. Look at nine areas that may hold clues about what's happening with your hair, and get personalized next steps."])])],
    "section bg-cream", anchor="navigator")

res_tools = res_section("tools", "Free tools", "Interactive quizzes and tools you can use right now. Answer a few questions and see what may deserve a closer look.",
                        '[thln_resources section="tools"]', "bg-white")
res_downloads = res_section("downloads", "Free downloads", "Guides and worksheets to keep, use and bring to your appointments.",
                            '[thln_resources section="downloads"]', "bg-cream")

# ------------------------------------------------------------------ OUTPUT
PARTS_MAP = {
    "home-hero": home_hero, "home-problem": home_problem, "home-deep-roots": home_deep_roots,
    "home-roots": home_roots, "home-path": home_path, "home-holly": home_holly, "home-final-cta": home_final,
    "about-hero": about_hero, "about-story": about_story, "about-question": about_question, "about-quote": about_quote,
    "about-before-after": about_before_after, "about-believe": about_believe, "about-why": about_why,
    "about-nutrition": about_nutrition, "about-start-here": about_start, "about-talk": about_talk,
    "contact-main": contact_main, "navigator-band": navigator_band,
    "resources-hero": res_hero, "resources-guides": res_guides, "resources-navigator": res_navigator,
    "resources-tools": res_tools, "resources-downloads": res_downloads,
}

# (slug, title, category, parts, is_page_starter, description)
PATTERNS_LIST = [
    ("homepage", "Homepage (full page)", "thln-pages",
     ["home-hero", "home-problem", "home-deep-roots", "home-roots", "home-path", "home-holly", "home-final-cta"], True,
     "The complete homepage, ready to edit."),
    ("about-page", "About page (full page)", "thln-pages",
     ["about-hero", "about-story", "about-question", "about-quote", "about-before-after", "about-believe",
      "about-why", "about-nutrition", "about-start-here", "about-talk"], True, "The complete About page."),
    ("contact-page", "Contact page (full page)", "thln-pages", ["contact-main", "navigator-band"], True,
     "Contact page. Add your WPForms form where the placeholder says."),
    ("resources-page", "Resources page (full page)", "thln-pages",
     ["resources-hero", "resources-guides", "resources-navigator", "resources-tools", "resources-downloads"], True,
     "Resources page. The cards come from Resources in the admin menu."),
    ("section-hero", "Home: hero", "thln-sections", ["home-hero"], False, ""),
    ("section-problem", "Home: advice overload", "thln-sections", ["home-problem"], False, ""),
    ("section-deep-roots", "DEEP ROOTS grid", "thln-sections", ["home-deep-roots"], False, ""),
    ("section-roots", "ROOTS framework", "thln-sections", ["home-roots"], False, ""),
    ("section-path", "A path forward", "thln-sections", ["home-path"], False, ""),
    ("section-holly", "Hi, I'm Holly", "thln-sections", ["home-holly"], False, ""),
    ("section-final-cta", "Closing call to action (plum)", "thln-sections", ["home-final-cta"], False, ""),
    ("section-navigator-feature", "DEEP ROOTS Navigator feature", "thln-sections", ["resources-navigator"], False, ""),
    ("section-navigator-band", "DEEP ROOTS Navigator banner", "thln-sections", ["navigator-band"], False, ""),
    ("section-story", "Story block (label + text)", "thln-sections", ["about-story"], False, ""),
    ("section-quote-band", "Big quote band (plum)", "thln-sections", ["about-quote"], False, ""),
]


def main():
    os.makedirs(PARTS, exist_ok=True)
    os.makedirs(PATTERNS, exist_ok=True)
    for f in os.listdir(PATTERNS):
        if f.endswith(".php"):
            os.remove(os.path.join(PATTERNS, f))
    for name, markup in PARTS_MAP.items():
        with open(os.path.join(PARTS, name + ".php"), "w") as fh:
            fh.write("<?php defined( 'ABSPATH' ) || exit; ?>\n" + markup)
    for slug, title, cat, parts, starter, desc in PATTERNS_LIST:
        head = ["<?php", "/**", f" * Title: {title}", f" * Slug: thln/{slug}", f" * Categories: {cat}"]
        if desc:
            head.append(f" * Description: {desc}")
        if starter:
            head += [" * Block Types: core/post-content", " * Post Types: page"]
        head += [" * Viewport Width: 1400", " */", "defined( 'ABSPATH' ) || exit;", "?>"]
        body = "".join(f"<?php include get_theme_file_path( 'parts/{x}.php' ); ?>\n" for x in parts)
        with open(os.path.join(PATTERNS, slug + ".php"), "w") as fh:
            fh.write("\n".join(head) + "\n" + body)
    print(f"{len(PARTS_MAP)} parts, {len(PATTERNS_LIST)} patterns")


if __name__ == "__main__":
    main()
