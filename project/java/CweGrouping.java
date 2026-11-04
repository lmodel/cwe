package example;

/* metamodel_version: 1.12.0 */
/* version: 5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A set of weaknesses gathered by something they share, for browsing and not for mapping real vulnerabilities to. Schema versions before 8.0 called it a category.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweGrouping extends CweEntry {

  private String summary;
  private CweRelationships relationships;
  private List<CweTaxonomyMapping> taxonomyMappings;


}