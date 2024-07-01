package classtest.musicChart;

public class Song {
	private String title;
	private String singer;
	private String releaseDate;
	
	public String getTitle() {
		return this.title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getReleaseDate() {
		return this.releaseDate;
	}

	public void setReleaseDate(String releaseDate) {
		this.releaseDate = releaseDate;
	}

	public String getSinger() {
		return this.singer;
	}

	public void setSinger(String singer) {
		this.singer = singer;
	}
	
	public Song(String title, String singer, String releaseDate) {
		this.setTitle(title);
		this.setReleaseDate(releaseDate);
		this.setSinger(singer);
	}
	
	public void printInfo() {
		System.out.printf("제목=%s | 가수=%s | 발매일=%s\n", this.getTitle(), this.getSinger(), this.getReleaseDate());
	}
}
