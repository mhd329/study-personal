package classtest.worker;

public class Worker {
	private String name;
	private int career;
	private Job job;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getCareer() {
		return career;
	}
	public void setCareer(int career) {
		this.career = career;
	}
	public Job getJob() {
		return job;
	}
	public void setJob(Job job) {
		this.job = job;
	}
	
	public Worker(String name, int career, Job job) {
		this.setName(name);
		this.setCareer(career);
		this.setJob(job);
	}
	
	public void printInfo() {
		System.out.printf("이름=%-10s\t| 커리어=%-10s\t| 직업=%-10s\n", this.getName(), this.getCareer(), this.getJob());
	}
	
}
