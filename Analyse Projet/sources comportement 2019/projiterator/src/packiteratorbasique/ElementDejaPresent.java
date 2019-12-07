package packiteratorbasique;

public class ElementDejaPresent extends Exception	 
{
	private static final long serialVersionUID = 9223372036854775807L;	
	 

	public ElementDejaPresent(Personne elt) 
	{	super("La personne s'appelant " + elt.toString() + " est déjà présente dans l'agenda \n");	}
}

