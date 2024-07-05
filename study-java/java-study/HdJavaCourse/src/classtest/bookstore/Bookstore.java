package classtest.bookstore;

import classtest.order.DecimalUtil;

public class Bookstore {
	private Book[] bookArray;
	
	public Book[] getBookArray() {
		return bookArray;
	}

	public void setBookArray(Book[] bookArray) {
		this.bookArray = bookArray;
	}

	public Bookstore(Book[] bookArray) {
		this.setBookArray(bookArray);
	}
	
	private void printCase(String category) {
		switch (category) {
			case "comic" -> {
				System.out.println("분야=만화");
			}
			case "travel" -> {
				System.out.println("분야=여행");
			}
			case "food" -> {
				System.out.println("분야=음식");
			}
			case "health" -> {
				System.out.println("분야=건강");
			}
			case "pc" -> {
				System.out.println("분야=컴퓨터");
			}
			case "etc" -> {
				System.out.println("분야=기타");
			}
			default -> {
				System.out.println("분야=없음");
			}
		}
	}
	
	public void printInfo() {
		for (int i = 0; i < this.bookArray.length; i ++) {
			String category = this.bookArray[i].getCategory();
			String title = this.bookArray[i].getTitle();
			String author = this.bookArray[i].getAuthor();
			String publisher = this.bookArray[i].getPublisher();
			int price = this.bookArray[i].getPrice();
			
			String won = DecimalUtil.decimalComma(price);
			
			String isbn = this.bookArray[i].getIsbn();
			System.out.printf("%d.\n", i + 1);
			this.printCase(category);
			System.out.printf("제목=%s\n", title);
			System.out.printf("저자=%s\n", author);
			System.out.printf("출판사=%s\n", publisher);
			System.out.printf("가격=%s(원)\n", won);
			System.out.printf("isbn=%s\n", isbn);
		}
	}
	
	public void printInfo(int i, int idx) {
		String category = this.bookArray[i].getCategory();
		String title = this.bookArray[i].getTitle();
		String author = this.bookArray[i].getAuthor();
		String publisher = this.bookArray[i].getPublisher();
		int price = this.bookArray[i].getPrice();
		
		String won = DecimalUtil.decimalComma(price);
		
		String isbn = this.bookArray[i].getIsbn();
//		System.out.printf("%d.\n", i + 1);
		System.out.printf("%d.\n", idx);
		this.printCase(category);
		System.out.printf("제목=%s\n", title);
		System.out.printf("저자=%s\n", author);
		System.out.printf("출판사=%s\n", publisher);
		System.out.printf("가격=%s(원)\n", won);
		System.out.printf("isbn=%s\n", isbn);
	}
	
	public void printBooksByIsbn(String isbn) {
		int idx = 1;
		boolean notPrint = false;
		for (int i = 0; i < this.bookArray.length; i ++) {
			if (this.bookArray[i].getIsbn() == isbn) {
				printInfo(i, idx);
				idx += 1;
			}
		}
		if (notPrint) {			
			System.out.println("\nNo data available.\n");
		}
	}
	
	public void printBooksByBetweenPrice(int minPrice, int maxPrice) {
		int idx = 1;
		boolean notPrint = false;
		for (int i = 0; i < this.bookArray.length; i ++) {
			int price = this.bookArray[i].getPrice();
			if (price >= minPrice && price <= maxPrice) {
				printInfo(i, idx);
				idx += 1;
			}
		}
		if (notPrint) {			
			System.out.println("\nNo data available.\n");
		}
	}
	
	public void printBooksByCategory(String category) {
		int idx = 1;
		boolean notPrint = false;
		for (int i = 0; i < this.bookArray.length; i ++) {
			if (this.bookArray[i].getCategory() == category) {
				printInfo(i, idx);
				idx += 1;
			}
		}
		if (notPrint) {			
			System.out.println("\nNo data available.\n");
		}
	}
	
	public void printBooksByMaxUnderPrice(int maxPrice) {
		int idx = 1;
		boolean notPrint = false;
		for (int i = 0; i < this.bookArray.length; i ++) {
			if (this.bookArray[i].getPrice() <= maxPrice) {
				printInfo(i, idx);
				idx += 1;
			}
		}
		if (notPrint) {			
			System.out.println("\nNo data available.\n");
		}
	}
	
	public void printBooksByMinUpPrice(int minPrice) {
		int idx = 1;
		boolean notPrint = false;
		for (int i = 0; i < this.bookArray.length; i ++) {
			if (this.bookArray[i].getPrice() >= minPrice) {
				printInfo(i, idx);
				idx += 1;
			}
		}
		if (notPrint) {			
			System.out.println("\nNo data available.\n");
		}
	}
	
	public void printBooksByTitleLike(String title) {
		int idx = 1;
		boolean notPrint = false;
		for (int i = 0; i < this.bookArray.length; i ++) {
			if (this.bookArray[i].getTitle().indexOf(title) != -1) {
				printInfo(i, idx);
				idx += 1;
			}
		}
		if (notPrint) {			
			System.out.println("\nNo data available.\n");
		}
	}
	
}
