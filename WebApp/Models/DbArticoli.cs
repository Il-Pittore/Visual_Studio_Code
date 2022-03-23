using Microsoft.EntityFrameworkCore;

namespace WebApp.Models;
public class DbArticoli : DbContext
	{
		public DbSet<Articolo> Articoli { get; set; }
		public DbArticoli (DbContextOptions<DbArticoli> options)
			: base(options)
		{
		}
	}
