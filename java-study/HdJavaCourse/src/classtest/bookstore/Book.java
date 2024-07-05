package classtest.bookstore;

public class Book {
	private String category;
	private String title;
	private String author;
	private String publisher;
	private int price;
	private String isbn;
	
	public String getCategory() {
		return category;
	}
	public void setCategory(String category) {
		this.category = category;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getAuthor() {
		return author;
	}
	public void setAuthor(String author) {
		this.author = author;
	}
	public String getPublisher() {
		return publisher;
	}
	public void setPublisher(String publisher) {
		this.publisher = publisher;
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
	public String getIsbn() {
		return isbn;
	}
	public void setIsbn(String isbn) {
		this.isbn = isbn;
	}
	
	public Book(String category, String title, String author, String publisher, int price, String isbn) {
		this.setCategory(category);
		this.setTitle(title);
		this.setAuthor(author);
		this.setPublisher(publisher);
		this.setPrice(price);
		this.setIsbn(isbn);
	}
	
	
	
}
