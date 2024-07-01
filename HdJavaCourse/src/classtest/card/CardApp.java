package classtest.card;

public class CardApp {

	public static void main(String[] args) {
		Cards c = new Cards();
		String[] cards = c.getCards();

		for (int i = 0; i < 13; i ++) {
			System.out.printf("cardRanks[%d] : %s\n", i, cards[i]);
		}
		
	}

}
