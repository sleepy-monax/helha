package packiteratorbasique;
import java.util.List;

public class IteratorPersonne 
{
	private int index;	
	private List<Personne> liste;
	
	
	public IteratorPersonne(List<Personne> liste) 
	{	
		super();					
		this.liste = liste;
	}
	
	
	public Personne item() 			
	{
		if (index >= 0 && index < liste.size())		 
		{	return liste.get(index);}			
		else 
		{	return null;					}			
												
	}
	
	public void next() 
	{	index++;	}
		

	public void preview() 
	{	index--;							}
	
	public int indexDernier()
	{	return index = liste.size() - 1;	}
	
	public int getIndex()
	{	return index;						}
	
	
	public int getNbIndex()
	{	return liste.size();				}

}
