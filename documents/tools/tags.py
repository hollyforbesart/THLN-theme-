"""The 10 nutrient tags: (slug, label, soft background, dark ink).

Shared by both documents. Change a color here and rebuild to update everywhere."""
TAGS = [
    ("protein",  "Protein",        "#F8DCD2", "#8A3A22"),  # coral
    ("carbs",    "Carbohydrates",  "#F5E5C0", "#6E4E0E"),  # wheat
    ("iron",     "Iron",           "#F4D2DB", "#8A2440"),  # rose
    ("zinc",     "Zinc",           "#DDE2F4", "#33427A"),  # periwinkle
    ("vitd",     "Vitamin D",      "#FAEDB0", "#665200"),  # sunshine
    ("b12",      "Vitamin B12",    "#D2E7F4", "#1D5676"),  # sky
    ("vitc",     "Vitamin C",      "#FBDCC0", "#8A4306"),  # tangerine
    ("biotin",   "Biotin",         "#E7DBF3", "#5A3A7E"),  # lilac
    ("omega3",   "Omega-3",        "#CDEAE3", "#1C6255"),  # sea green
    ("folate",   "Folate",         "#DCEAC8", "#3D621F"),  # leaf
]
BY_LABEL = {t[1].lower(): t for t in TAGS}
