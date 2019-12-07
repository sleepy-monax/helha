package packiteratoraveccondition;

public class ElementDejaPresent extends Exception 
{
	private static final long serialVersionUID = 7391527175541321465L;

	public ElementDejaPresent(Personne elt) 
	{	super("La personne s'appelant " + elt.toString() + " est déjà présente dans l'agenda");	}
}
