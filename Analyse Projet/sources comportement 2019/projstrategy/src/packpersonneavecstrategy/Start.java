package packpersonneavecstrategy;

public class Start 
{
	public static void main(String[] args) 
	{
		Personne p = new Personne();				

		p.setDeplacement(new DeplacementMarche());	
		p.seDeplacer();								

		p.setDeplacement(new DeplacementCourse());				
		p.seDeplacer();															
		
		p.setDeplacement(new DeplacementArret());	
		p.seDeplacer();								
	}	
}


 