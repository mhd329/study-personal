package classtest.NestedClass;

public class Drink {

	private String category;
	
	public Drink(String category) {
		this.category = category;
	}
	
	public String getCategory() {
		return category;
	}
	
	public void setCategory(String category) {
		this.category = category;
	}
	
	public void printInfo() {
		System.out.println("category=" + category);
	}
	
	// ==============================
	// 중첩 클래스
	// ==============================
	public class Coffee {
		
		private String name;
			
		public Coffee(String name) {
			this.name = name;
		}
		
		public String getName() {
			return name;
		}
		
		public void setName(String name) {
			this.name = name;
		}
		
		public void printCoffeInfo() {
			System.out.println("name=" + name);
		}
		
		public void printCoffeeAllnfo() {
			System.out.println("name=" + name + " | category=" + Drink.this.category);
		}
	
	}

}