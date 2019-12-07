package packpersonnesansstrategy;

public class Personne 
{
	private int vitesse;
	private Deplacement deplacement;
	public enum Deplacement {ARRET, MARCHE, COURSE;};	
	
 
	public Personne() 
	{	vitesse = 0;	}			 
									

	public void setDeplacement(Deplacement deplacement) 
	{	this.deplacement = deplacement;	}
	
	
	public void seDeplacer() 
	{

		if (deplacement == Deplacement.ARRET) 
		{
			System.out.println("Je suis à l'arrêt !");
			setVitesse(0);
		}

		else if (deplacement == Deplacement.MARCHE) 
		{
			System.out.println("Je me déplace en marchant !");
			setVitesse(6);
		}

		else if (deplacement == Deplacement.COURSE) 
		{
			System.out.println("Je me déplace en courant !");
			setVitesse(12);
		}

		System.out.println(toString());
	}
	

	public void setVitesse(int vitesse) 
	{
		if (vitesse >= 0)
			this.vitesse = vitesse;
	}
		
	 
	public String toString() 
	{	return "Je me déplace à la vitesse de " + vitesse + " km/h";	}
}
