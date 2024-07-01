package classtest.musicChart;

public class SongApp {

	public static void main(String[] args) {
		Song[] SongArray = new Song[3];
		SongArray[0] = new Song("불타오르네", "BTS", "20160502");
		SongArray[1] = new Song("밤편지", "아이유", "20190324");
		SongArray[2] = new Song("낮 밤", "이영지", "20211029");		
		
		MusicChart mc = new MusicChart(SongArray);
		mc.printMusicChart();
	}

}
