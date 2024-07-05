package classtest.bookstore;

public class BookstoreApp {

	public static void main(String[] args) {
		Book[] bookArray = new Book[5];
		
		bookArray[0] = BookService.makeBook("comic",	"열혈강호",			"전극진,	양재현",	"대원씨아이",		4500,	"979-11-5754-926-9");
		bookArray[1] = BookService.makeBook("travel",	"뉴욕 100배 즐기기",	"홍지윤",			"알에이치코리아",	14400,	"978-89-255-8673-1");
		bookArray[2] = BookService.makeBook("travel",	"바르셀로나 지금이 좋아",	"정다운",			"중앙북스",		15000,	"978-89-991-7580-0");
		bookArray[3] = BookService.makeBook("food",		"오늘의 맥주",			"이성준",			"오운",			18000,	"979-11-92814-04-9");
		bookArray[4] = BookService.makeBook("food",		"버번 위스키의 모든 것",	"조승원",			"(주)교유당",		24000,	"979-11-90277-42-6");
	
		Bookstore bs = new Bookstore(bookArray);
		
		System.out.println("\n===== printBookByIsbn() =====");
		
		System.out.println("\n----- 979-11-90277-42-6 -----");
		bs.printBooksByIsbn("979-11-90277-42-6");
		System.out.println("\n----- 979-11-90277-42-7 -----");
		bs.printBooksByIsbn("979-11-90277-42-7");
		
		System.out.println("\n===== printBooksByBetweenPrice() =====");
		System.out.println("\n----- 5000 - 20000 -----");
		bs.printBooksByBetweenPrice(5000, 20000);
		System.out.println("\n----- 5000 - 20000 -----");
		bs.printBooksByBetweenPrice(50000, 200000);
		
		System.out.println("\n===== printBooksByCategory() =====");
		System.out.println("\n----- travel -----");
		bs.printBooksByCategory("travel");
		System.out.println("\n----- food -----");
		bs.printBooksByCategory("food");
		
		System.out.println("\n===== printBooksByMaxPrice() =====");
		System.out.println("\n----- 15000 -----");
		bs.printBooksByMaxUnderPrice(15000);
		System.out.println("\n----- 20000 -----");
		bs.printBooksByMaxUnderPrice(20000);
		
		System.out.println("\n===== printBooksByMinPrice() =====");
		System.out.println("\n----- 10000 -----");
		bs.printBooksByMinUpPrice(10000);
		System.out.println("\n----- 2000 -----");
		bs.printBooksByMinUpPrice(2000);
		
		System.out.println("\n===== printBooksByTitleLike() =====");
		System.out.println("\n----- 뉴욕 -----");
		bs.printBooksByTitleLike("뉴욕");
		
		System.out.println("\n===== printInfo() =====");
		bs.printInfo();
		
	}

}
