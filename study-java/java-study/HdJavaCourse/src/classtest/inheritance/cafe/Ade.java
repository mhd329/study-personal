package classtest.inheritance.cafe;

public class Ade extends Menu {

	private String ingredient;

	public String getIngredient() {
		return ingredient;
	}

	public void setIngredient(String ingredient) {
		this.ingredient = ingredient;
	}

	public Ade(String name, int price, String ingredient) {
		super(name, price);
		this.setIngredient(ingredient);;
	}
	
	@Override
	protected void printInfo() {
		super.printInfo();
		System.out.printf("| 재료=%-10s", this.ingredient);
	}
	
}
