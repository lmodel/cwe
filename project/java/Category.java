package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A collection of weaknesses grouped by a shared characteristic (CategoryType in XSD). Organizational mechanism only; not for mapping.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Category  {

  private int id;
  private String name;
  private String status;
  private String summary;
  private Relationship relationships;
  private List<TaxonomyMapping> taxonomyMappings;
  private List<CWEReference> references;
  private MappingNotes mappingNotes;
  private List<Note> notes;
  private ContentHistory contentHistory;

}