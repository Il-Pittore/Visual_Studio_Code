using System.ComponentModel.DataAnnotations;

namespace WebApp.Models;

public class Articolo
{
	public int ArticoloID{ get; set; }
	public string Descrizione { get; set; }
	public float GiustoPrezzo { get; set; }
	public float PrezzoUno { get; set; }
	public float PrezzoDue { get; set; }
	public DateTime DataAggiornamento {get; set;}

	public string UrlImmagine{ get; set; }
	public int Count {get; set;} = 0;
}
