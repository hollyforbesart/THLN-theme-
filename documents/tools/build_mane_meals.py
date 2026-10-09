"""Build mane-meals.html from the meal data below.

Edit the copy here, then run:
    python3 tools/build_mane_meals.py && node tools/render.js mane-meals.html dist/mane-meals-everyday-edition.pdf
"""
from html import escape
from pathlib import Path

from tags import TAGS

ROOT = Path(__file__).resolve().parent.parent
ORDER = [t[0] for t in TAGS]
SLUG = {t[1]: t[0] for t in TAGS}
NAME = {t[0]: t[1] for t in TAGS}


def tag(label):
    """'Omega-3 (ALA)' -> pill with the omega3 color; a trailing * is kept."""
    base = label.split(" (")[0].rstrip("*")
    return SLUG[base], label


def tags_html(labels):
    pills = sorted((tag(l) for l in labels), key=lambda t: ORDER.index(t[0]))
    return "".join(f'<span class="tag t-{s}">{escape(l)}</span>' for s, l in pills)


# (photo, name, ingredients or None, tags)
PAGES = [
    ("Breakfast", [
        ("For mornings when you're on the go", [
            ("image8", "Strawberry Overnight Oats",
             "Oats, Greek yogurt, fortified milk, strawberries, chia seeds, and walnuts.",
             ["Protein", "Carbohydrates", "Vitamin D*", "Vitamin B12", "Omega-3 (ALA)"]),
            ("image10", "Tropical Green Protein Smoothie",
             "Fortified milk or soy milk, protein powder, frozen mango, pineapple, spinach, and ground flaxseed.",
             ["Protein", "Carbohydrates", "Vitamin C", "Folate", "Omega-3 (ALA)", "Vitamin D*"]),
            ("image13", "Spinach + Egg Breakfast Burrito",
             "Scrambled eggs, tomatoes, spinach, and cheddar cheese in a whole-wheat tortilla, with orange slices or berries.",
             ["Protein", "Carbohydrates", "Biotin", "Vitamin B12", "Folate", "Vitamin C", "Zinc"]),
        ]),
        ("For mornings when you have a little more time", [
            ("image16", "Berry Crunch Yogurt Bowl",
             "Greek yogurt, fresh berries, granola, chia seeds, and pumpkin seeds.",
             ["Protein", "Carbohydrates", "Vitamin C", "Zinc", "Omega-3 (ALA)"]),
            ("image14", "Tropical Yogurt Bowl",
             "Greek yogurt, mango, pineapple, banana, granola, and pumpkin seeds.",
             ["Protein", "Carbohydrates", "Vitamin C", "Zinc"]),
            ("image15", "Apple Cinnamon Oats + Eggs",
             "Oatmeal made with fortified milk, diced apple, cinnamon, and ground flaxseed, with boiled eggs on the side.",
             ["Protein", "Carbohydrates", "Biotin", "Vitamin B12", "Omega-3 (ALA)", "Vitamin D*"]),
        ]),
    ]),
    ("Lunch", [
        ("For when you need a quick lunch", [
            ("image1", "Chicken Crunch Wrap",
             "Precooked chicken, whole-wheat tortilla, lettuce, shredded carrots, feta cheese, and Greek yogurt dressing.",
             ["Protein", "Carbohydrates", "Zinc"]),
            ("image6", "Chickpea + Egg Salad",
             "Chickpeas, boiled eggs, spinach, tomatoes, avocado, cucumbers, and blueberries.",
             ["Protein", "Carbohydrates", "Iron", "Folate", "Biotin", "Vitamin C"]),
            ("image17", "Tuna Salad Sandwich with Tomato, Cucumber + Feta Salad",
             "Canned light tuna, Greek yogurt or mayonnaise, whole-grain bread, tomato, cucumber, feta cheese, olive oil, and lemon juice.",
             ["Protein", "Carbohydrates", "Vitamin B12", "Vitamin C"]),
        ]),
        ("For lunches you want to make ahead of time", [
            ("image18", "Chicken + Quinoa Veggie Bowl",
             "Chicken, quinoa sautéed with onions, and grilled tomatoes, bell peppers, and zucchini.",
             ["Protein", "Carbohydrates", "Iron", "Folate", "Vitamin C"]),
            ("image5", "Turkey Chili Rice Bowl",
             "Turkey, kidney beans, rice, tomatoes, and a vegetable of your choice.",
             ["Protein", "Iron", "Zinc", "Carbohydrates", "Vitamin C", "Folate"]),
            ("image4", "Beef + Broccoli with Noodles",
             "Beef strips, whole-wheat noodles, frozen broccoli, carrots, and peppers.",
             ["Protein", "Iron", "Zinc", "Vitamin B12", "Carbohydrates", "Vitamin C"]),
        ]),
    ]),
    ("Dinner", [
        ("For when you barely feel like cooking dinner", [
            ("image20", "Chicken + Black Bean Quesadilla",
             "Whole-wheat tortilla filled with precooked chicken, black beans, shredded cheese, and spinach. Served with a small bowl of salsa and avocado.",
             ["Protein", "Carbohydrates", "Iron", "Folate", "Zinc", "Vitamin B12"]),
            ("image11", "Spinach + Cheese Tortilla Pizza",
             "Whole-wheat tortilla topped with tomato sauce, mozzarella, and fresh spinach.",
             ["Protein", "Carbohydrates", "Vitamin B12", "Folate", "Vitamin C"]),
            ("image9", "Turkey Burger + Sweet Potato Wedges",
             "Turkey patty, whole-grain bun, lettuce, tomato, and roasted sweet potatoes.",
             ["Protein", "Carbohydrates", "Zinc", "Iron", "Vitamin C"]),
        ]),
        ("For when you have time to make dinner", [
            ("image7", "Sweet Thai Chili Salmon with Rice + Green Beans",
             "Salmon glazed with sweet Thai chili sauce, seasoned rice, and green beans.",
             ["Protein", "Carbohydrates", "Vitamin B12", "Omega-3 (EPA/DHA)"]),
            ("image19", "Chicken Veggie Stir-Fry",
             "Chicken, fresh broccoli, peppers, carrots, and rice.",
             ["Protein", "Carbohydrates", "Vitamin C", "Folate"]),
            ("image21", "Garlic Chicken with Roasted Sweet Potatoes + Cauliflower",
             "Chicken thighs, sweet potatoes, and cauliflower.",
             ["Protein", "Carbohydrates", "Vitamin C", "Vitamin B12", "Zinc"]),
        ]),
    ]),
]

SNACKS = ("For when you need a snack between meals", [
    ("image3", "Apple + Peanut Butter", None, ["Carbohydrates", "Protein"]),
    ("image2", "Walnut, Cashew + Pumpkin Seed Trail Mix", None,
     ["Omega-3 (ALA)", "Zinc", "Carbohydrates", "Protein"]),
    ("image12", "Hummus + Vegetable Sticks", "Carrots, celery, and bell peppers.",
     ["Protein", "Carbohydrates", "Iron", "Vitamin C"]),
])

KEY = [
    ("protein", "Provides the amino acids needed to build keratin, the main protein in hair."),
    ("carbs", "Supply energy that helps fuel your body's normal functions, including hair growth."),
    ("iron", "Helps carry oxygen throughout the body, including to tissues that support hair growth."),
    ("zinc", "Supports cell growth, tissue repair, and normal hair follicle function."),
    ("vitd", "Plays a role in hair follicle cycling and normal immune function."),
    ("b12", "Supports red blood cell production and DNA synthesis, both important for rapidly dividing cells."),
    ("vitc", "Supports collagen production and helps your body absorb iron from plant foods."),
    ("biotin", "Helps your body metabolize nutrients for energy and supports normal cell function."),
    ("omega3", "Provide essential fats used in cell membranes and help regulate inflammatory processes."),
    ("folate", "Supports DNA synthesis and cell division, processes needed for normal hair follicle activity."),
]
KEY_NAME = {"omega3": "Omega-3 Fatty Acids"}

VITD_NOTE = ("*Vitamin D content depends on the type and fortification of the milk or milk "
             "alternative used. Check the product label.")
HIGHLIGHTS_NOTE = ("The nutrient highlights show which of the 10 nutrients the foods in each meal "
                   "contribute. They aren't guaranteed amounts, and they aren't meant to correct a deficiency.")
DISCLAIMER = ("These meal ideas are meant to support your overall nutrition. They aren't intended to "
              "diagnose, treat, or reverse hair loss.")


def meal(photo, name, ingredients, labels):
    ing = f'<p class="meal__ing">{escape(ingredients)}</p>' if ingredients else ""
    return f"""
      <article class="meal">
        <img class="meal__photo" src="assets/photos/{photo}.jpg" alt="">
        <div class="meal__body">
          <h3>{escape(name)}</h3>{ing}
          <div class="tags">{tags_html(labels)}</div>
        </div>
      </article>"""


def category(title, meals):
    return f"""
    <section class="cat">
      <h2 class="cat__title">{escape(title)}</h2>{"".join(meal(*m) for m in meals)}
    </section>"""


def folio(n):
    return (f'<footer class="folio"><span><b>Mane Meals</b> · The Everyday Edition</span>'
            f'<span>thehairlossnutritionist.com</span><span>{n}</span></footer>')


def build():
    out = []
    page_no = 4
    for label, cats in PAGES:
        has_vitd = any("Vitamin D*" in m[3] for _, ms in cats for m in ms)
        note = f'<p class="footnote">{escape(VITD_NOTE)}</p>' if has_vitd else ""
        out.append(f"""
<section class="page meals-page">
  <div class="inner">
    <header class="meals-head"><p class="eyebrow">The Mane Meals</p><h1>{label}</h1></header>
    {"".join(category(*c) for c in cats)}
    {note}
  </div>
  {folio(page_no)}
</section>""")
        page_no += 1

    key = "".join(
        f"""
        <li class="key__item t-{s}">
          <img src="assets/icons/{s}.png" alt="">
          <div><h3>{escape(KEY_NAME.get(s, NAME[s]))}</h3>
          <p>{escape(d)}</p></div>
        </li>""" for s, d in KEY)

    snacks_title, snacks = SNACKS
    html = (ROOT / "tools" / "mane_meals_template.html").read_text()
    html = (html.replace("{{MEAL_PAGES}}", "".join(out))
                .replace("{{KEY}}", key)
                .replace("{{SNACKS}}", category(snacks_title, snacks))
                .replace("{{HIGHLIGHTS_NOTE}}", escape(HIGHLIGHTS_NOTE))
                .replace("{{DISCLAIMER}}", escape(DISCLAIMER))
                .replace("{{FOLIO2}}", folio(2))
                .replace("{{FOLIO3}}", folio(3))
                .replace("{{FOLIO7}}", folio(7)))
    (ROOT / "mane-meals.html").write_text(html)
    count = sum(len(ms) for _, cats in PAGES for _, ms in cats) + len(snacks)
    print(f"mane-meals.html written ({count} ideas)")


if __name__ == "__main__":
    build()
