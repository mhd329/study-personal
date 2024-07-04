package classtest.bookstore;

public class BookService {
	public static Book makeBook(String category, String title, String author, String publisher, int price, String isbn) {
		Book book = new Book(category, title, author, publisher, price, isbn);
		return book;
	}
}
