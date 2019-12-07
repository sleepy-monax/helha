package packiteratoraveccondition;

import java.util.List;

public class IteratorPersonne
{
	
	private String motCle;
	private int index;					
	private List<Personne> liste;
	

	public IteratorPersonne(List<Personne> liste, String motCl) 
	{
		super();
		this.liste = liste;
		setMotCle(motCl);			// doit initialiser le critère avant de faire la recherche
		start();
		
	}
	
	
	
	public Personne item() 
	{
		if (index < liste.size()) 
		{	return liste.get(index);		}
		else 
		{	return null;					}
	}

	
	public void setMotCle(String motCle) 
	{	this.motCle = motCle;		}
	
	// Récupère la 1ère personne en fonction du critère, 
	// on retiendra en fait la valeur de INDEX, dans le sens 
	// qu'on s'arrete dessus en fonction de index++
	public void start() 
	{
		for (;;) 		
		{
			Personne p = item();
			p = item();
			if (p == null)				 
			{	return;			}
			
			if (p.plusGrand(motCle)) 
			{	return;			}		 
										
			index++;					
		}
	}
	
	// Recherche de l'élément suivant correspondant au critère demandé 
	public void next() 
	{
		index++;
		for (;;) 
		{
			Personne p = item();
			if (p == null) 
			{	return;				}
			
			if (p.plusGrand(motCle)) 
			{	return;				}
			
			index++;
		}
	}
}