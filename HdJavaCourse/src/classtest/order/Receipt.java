package classtest.order;

public class Receipt {
	private Menu[] order;
	
	public Menu[] getOrder() {
		return this.order;
	}
	
	public void setOrder(Menu[] order) {
		this.order = order;
	}

	public Receipt(Menu[] order) {
		this.setOrder(order);
	}
	
	public void printOrderInfo() {
		int sum = 0;
		System.out.println("===== [영수증] =====");
		System.out.println("----- 주문 시간 -----");
		System.out.println(DateUtil.getLocalDateTimeDash());
		System.out.println();
		
		System.out.println("----- 주문 상세 -----");
		for (Menu m: order) {
			int price = m.getPrice();
			System.out.printf("메뉴=%s | 가격=%s\n", m.getName(), DecimalUtil.decimalComma(price));
			sum += price;
		}
		
		System.out.println();
		System.out.println("----- 주문 금액 합계 -----");
		System.out.printf("%s(원)", DecimalUtil.decimalComma(sum));
	}
}
