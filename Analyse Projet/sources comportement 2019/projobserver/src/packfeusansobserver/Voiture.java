package packfeusansobserver;
import packfeusansobserver.Feu.Couleur;

public class Voiture 
{
	private Feu feuDevantV;

	public void setFeuDevantV(Feu feuDevantFS) 
	{	this.feuDevantV = feuDevantFS;		}
	
	public void demarrer() 
	{
		System.out.println("Je tente de démarrer. ");
		if (feuDevantV == null || feuDevantV.getCouleur() == Couleur.VERT) 
		{
			System.out.println("     Je roule");		
			setFeuDevantV(null);		        	
			return;
		}
	}
	
	public void sarreter() 
	{	System.out.println("Je m'arrête");	}
}
