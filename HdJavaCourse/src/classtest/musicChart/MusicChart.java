package classtest.musicChart;
//import java.text.SimpleDateFormat;
//import java.util.Date;

public class MusicChart {
	private Song[] songArray;
	
	public Song[] getSongArray() {
		return this.songArray;
	}

	public void setSongArray(Song[] songArray) {
		this.songArray = songArray;
	}

	public MusicChart(Song[] songArray) {
		this.setSongArray(songArray);
	}
	
	public void printMusicChart() {
		for (Song s: this.songArray) {
//			SimpleDateFormat sdfOld = new SimpleDateFormat("yyyyMMdd");
//			SimpleDateFormat sdfNew = new SimpleDateFormat("yyyy.MM.dd");
//			try {
//				Date releaseDate = sdfOld.parse(s.getReleaseDate());
//				String newReleaseDate = sdfNew.format(releaseDate);
//				System.out.printf("제목=%s | 가수=%s | 발매일=%s\n", s.getTitle(), s.getSinger(), newReleaseDate);
//				System.out.println();
//			} catch (Exception e) {
//				System.out.println(e.getMessage());
//			}
			String yyyy = s.getReleaseDate().substring(0, 4);
			String mm = s.getReleaseDate().substring(4, 6);
			String dd = s.getReleaseDate().substring(6, 8);
			System.out.printf("제목=%s | 가수=%s | 발매일=%s.%s.%s\n", s.getTitle(), s.getSinger(), yyyy, mm, dd);
		}
	}
}
