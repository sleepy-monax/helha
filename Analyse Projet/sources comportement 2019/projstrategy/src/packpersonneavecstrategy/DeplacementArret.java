package packpersonneavecstrategy;

public class DeplacementArret implements Deplacement 
{

	@Override
	public void seDeplacer(Personne p) 
	{	
		System.out.println("Je suis à l'arrêt !");
		p.setVitesse(0);
	}
}
