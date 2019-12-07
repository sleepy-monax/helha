package packiteratoraveccondition;
import java.util.ArrayList;

public class Agenda 
{

	private ArrayList<Personne> liste;
	
	public Agenda() 
	{	liste = new ArrayList<Personne>();	}
	
	public void ajouter(Personne elt) throws ElementDejaPresent 
	{	
		if (!liste.contains(elt)) 		 
		{	liste.add(elt);									}
		else 
		{	throw new ElementDejaPresent(elt);				}
	}
	


	public IteratorPersonne creerIterateur(String motC) 
	{	return new IteratorPersonne(liste, motC);			}
	

	public IteratorPersonne rechercheAlpha(String motCle) 		
	{	
		IteratorPersonne iterateur = creerIterateur(motCle);
		return iterateur; 											
	}
}