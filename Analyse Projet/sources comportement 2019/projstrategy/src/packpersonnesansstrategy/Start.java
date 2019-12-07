package packpersonnesansstrategy;
import packpersonnesansstrategy.Personne.Deplacement;

public class Start 
{
	public static void main(String[] args) 
	{
		Personne p = new Personne();				 
 		
		p.setDeplacement(Deplacement.MARCHE);		
 		p.seDeplacer();								
													
		
		p.setDeplacement(Deplacement.COURSE);		
 		p.seDeplacer();								
													
		
		p.setDeplacement(Deplacement.ARRET);		
 		p.seDeplacer();								
													
	}
}