package classtest.song;

public class Song {
	private String title;
	private String releaseDate;
	private Singer singer;
	
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

	public Singer getSinger() {
		return this.singer;
	}

	public void setSinger(Singer singer) {
		this.singer = singer;
	}
	
	public Song(String title, Singer singer, String releaseDate) {
		this.setTitle(title);
		this.setReleaseDate(releaseDate);
		this.setSinger(singer);
	}
	
	public void printInfo() {
		System.out.printf("제목=%s | 발매일=%s\n", this.getTitle(), this.getReleaseDate());
		this.singer.printInfo();
	}

}
