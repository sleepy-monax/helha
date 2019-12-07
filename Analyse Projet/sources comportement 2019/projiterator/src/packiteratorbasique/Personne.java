package packiteratorbasique;
public class Personne
{

	private String nom;
	private String prenom;
	

	public Personne(String nom, String prenom) 
	{
		super();				
		this.nom = nom;			
		this.prenom = prenom; 	 
	}
	
	public String toString() 
	{	return prenom + " " + nom;	}
	
	public boolean equals(Object o) 
	{
		if (o instanceof Personne) 
		{							
			Personne p = (Personne)o;
			return this.nom.equals(p.nom) && this.prenom.equals(p.prenom);
		}
		else { return false; }
	}
}