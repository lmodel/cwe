package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A perspective from which to look at weaknesses in the catalog (ViewType in XSD). Types: Graph, Explicit slice, Implicit slice.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class View  {

  private int id;
  private String name;
  private String type;
  private String status;
  private String objective;
  private List<Audience> audience;
  private List<CatalogMember> members;
  private String filter;
  private List<CWEReference> references;
  private MappingNotes mappingNotes;
  private List<Note> notes;
  private ContentHistory contentHistory;

}