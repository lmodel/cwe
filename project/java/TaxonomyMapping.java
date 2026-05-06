package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A mapping from a CWE entry to an equivalent entry in an external taxonomy (TaxonomyMappingsType/Taxonomy_Mapping in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaxonomyMapping  {

  private String taxonomyName;
  private String entryId;
  private String entryName;
  private String mappingFit;

}