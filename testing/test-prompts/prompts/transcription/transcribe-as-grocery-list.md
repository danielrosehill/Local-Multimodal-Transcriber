# Transcribe as Grocery List

**Tests:** Format transformation, item extraction, categorization, quantity identification

---

Listen to this audio recording and convert its content into an organized grocery shopping list.

Transform the spoken content into grocery list format:

## Grocery List Structure

Organize items by store section/category:

**Produce**
- Item (quantity/amount if specified)

**Dairy & Eggs**
- Item (quantity/amount if specified)

**Meat & Seafood**
- Item (quantity/amount if specified)

**Bakery**
- Item (quantity/amount if specified)

**Pantry/Dry Goods**
- Item (quantity/amount if specified)

**Frozen**
- Item (quantity/amount if specified)

**Beverages**
- Item (quantity/amount if specified)

**Household/Non-Food**
- Item (quantity/amount if specified)

**Other**
- Item (quantity/amount if specified)

## Formatting rules:

1. **Quantities**: Include if mentioned (e.g., "2 lbs chicken", "1 dozen eggs", "large bag")
2. **Specifics**: Note brand preferences, varieties, or requirements (e.g., "organic", "whole wheat", "unsalted")
3. **Alternatives**: If speaker mentions backup options, note as "or [alternative]"
4. **Urgency**: Mark items mentioned as urgent or "don't forget" with a star (*)

Preserve:
- All items mentioned, even in passing
- Exact quantities and specifications
- Brand names or preferences stated
- Recipe-related context (e.g., "for the pasta dish")

Adapt:
- Stream-of-consciousness mentions to organized categories
- Vague quantities to practical shopping amounts where obvious
- Rambling descriptions to concise list entries

The result should be ready to use while shopping.
