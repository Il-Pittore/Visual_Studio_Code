using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using WebApp.Models;

namespace WebApp.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class GiocoUnoController : ControllerBase
    {
        private readonly DbArticoli _context;

        public GiocoUnoController(DbArticoli context)
        {
            _context = context;
        }

        // GET: api/GiocoUno
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Articolo>>> GetArticoli()
        {
            return await _context.Articoli.ToListAsync();
        }

        // GET: api/GiocoUno/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Articolo>> GetArticolo(int id)
        {
            var articolo = await _context.Articoli.FindAsync(id);

            if (articolo == null)
            {
                return NotFound();
            }

            return articolo;
        }

        // PUT: api/GiocoUno/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutArticolo(int id, Articolo articolo)
        {
            if (id != articolo.ArticoloID)
            {
                return BadRequest();
            }

            _context.Entry(articolo).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!ArticoloExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/GiocoUno
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Articolo>> PostArticolo(Articolo articolo)
        {
            _context.Articoli.Add(articolo);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetArticolo", new { id = articolo.ArticoloID }, articolo);
        }

        // DELETE: api/GiocoUno/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteArticolo(int id)
        {
            var articolo = await _context.Articoli.FindAsync(id);
            if (articolo == null)
            {
                return NotFound();
            }

            _context.Articoli.Remove(articolo);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool ArticoloExists(int id)
        {
            return _context.Articoli.Any(e => e.ArticoloID == id);
        }
    }
}
