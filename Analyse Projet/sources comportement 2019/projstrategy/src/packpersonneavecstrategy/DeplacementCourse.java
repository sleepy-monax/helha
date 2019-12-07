package packpersonneavecstrategy;

public class DeplacementCourse implements Deplacement 
{

	@Override
	public void seDeplacer(Personne p) 
	{
		System.out.println("Je me déplace en courant !");
		p.setVitesse(12);
	}
}
