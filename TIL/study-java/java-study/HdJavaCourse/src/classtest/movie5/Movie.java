package classtest.movie5;

public class Movie {
	private String title;
	private String category;
	private String director;
	private Actor[] actorArray;
	private int runningTime;
	
	public String getTitle() {
		return this.title;
	}
	
	public void setTitle(String title) {
		this.title = title;
	}
	
	public String getDirector() {
		return this.director;
	}
	
	public void setDirector(String director) {
		this.director = director;
	}
	
	public String getCategory() {
		return this.category;
	}
	
	public void setCategory(String category) {
		this.category = category;
	}
	
	public Actor[] getActorArray() {
		return this.actorArray;
	}
	
	public void setActorArray(Actor[] actorArray) {
		this.actorArray = actorArray;
	}
	
	public int getRunningTime() {
		return this.runningTime;
	}
	
	public void setRunningTime(int runningTime) {
		if (runningTime < 0) {			
			System.out.println("러닝타임은 -1보다 큰 정수여야합니다.");
		} else {
			this.runningTime = runningTime;
		}
	}
	
	public Movie(String title, String category, String director, int runningTime, Actor[] actorArray) {
		this.setTitle(title);
		this.setCategory(category);
		this.setDirector(director);
		this.setActorArray(actorArray);
		this.setRunningTime(runningTime);
	}
	
	public void printInfo() {
		System.out.printf("제목=%s | 분류=%s | 감독=%s | 상영시간=%d(분)\n", this.getTitle(), this.getCategory(), this.getDirector(), this.getRunningTime());
		for (Actor actor: this.getActorArray()) {
			actor.printInfo();
		}
	}
}
