package packpersonneavecstrategy;

public class Personne 
{
	private int vitesse;
	private Deplacement deplacement;
	

	public Personne() 
	{	vitesse = 0;	}	

	
	public void setDeplacement(Deplacement deplacement) 
	{	this.deplacement = deplacement;	}
	
	public void seDeplacer() 
	{
		if (deplacement != null) 
		{
			deplacement.seDeplacer(this);			
			System.out.println(this.toString());	
		}											
	}
	

	public void setVitesse(int vitesse) 
	{
		if (vitesse >= 0)
			this.vitesse = vitesse;
	}
		

	public String toString() 
	{	return "Je me déplace à la vitesse de " + vitesse + " km/h";	}
}
