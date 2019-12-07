package packfeuavecobserver;
public class Feu extends Observable 	
{

	private Couleur couleur;
	public enum Couleur {VERT, ORANGE, ROUGE;}
	
	public Feu() 
	{	
		super(); 
		couleur = Couleur.VERT;	
	}
	
	public void changeCouleur() 
	{
		switch (couleur) 
		{
			case VERT : couleur = Couleur.ORANGE; break;
			case ORANGE : couleur = Couleur.ROUGE; break;
			case ROUGE : couleur = Couleur.VERT; notifie(); break;	
		}
	}
	
	public Couleur getCouleur() 
	{	return couleur;		}
	
}