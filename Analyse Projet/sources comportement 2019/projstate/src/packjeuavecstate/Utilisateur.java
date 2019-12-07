package packjeuavecstate;

public class Utilisateur 
{
	private String pseudo, motPasse;

	public Utilisateur(String pseudo, String motPasse) 
	{
		this.pseudo = pseudo;
		this.motPasse = motPasse;
	}
	
	public String toString() 
	{	return pseudo+" "+motPasse;		}
}