package classtest.movie4;

public class Movie {
	private String title;
	private String category;
	private String director;
	private Actor actor;
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
	
	public Actor getActor() {
		return this.actor;
	}
	
	public void setActor(Actor actor) {
		this.actor = actor;
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
	
	public Movie(String title, String category, String director, int runningTime, Actor actor) {
		this.setTitle(title);
		this.setCategory(category);
		this.setDirector(director);
		this.setActor(actor);
		this.setRunningTime(runningTime);
	}
	
	public void printInfo() {
		System.out.println(this.getTitle());
		System.out.println(this.getCategory());
		System.out.println(this.getDirector());
		System.out.println(this.getRunningTime());
		System.out.println("여기는액터");
		this.actor.printInfo();
	}

}