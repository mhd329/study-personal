package classtest.coffee;

public class Coffee {

	public static void main(String[] args) {
		CoffeeModel ame = new CoffeeModel();
		ame.setCoffee("아메리카노");
		ame.setPrice(2000);
		ame.setOrder("샷추가, 아이스, 디카페인");
		
		ame.printInfo();

	}

}
