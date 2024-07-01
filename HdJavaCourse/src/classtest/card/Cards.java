package classtest.card;

public class Cards {
	private String[] cardRanks;
	
	public String[] getCards() {
		return this.cardRanks;
	}
	
	public Cards() {
		this.cardRanks = new String[13];
		this.setArray();
	}
	
	private void setArray() {
		for (int i = 0; i < 10; i ++) {
			cardRanks[i] = String.valueOf(i + 1);
		}
		cardRanks[10] = "Jack";
		cardRanks[11] = "Queen";
		cardRanks[12] = "King";
		
	}
	
}
