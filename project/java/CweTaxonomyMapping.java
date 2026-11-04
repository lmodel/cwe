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
  A link from an entry to an entry of another taxonomy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweTaxonomyMapping  {

  private String taxonomyName;
  private String entryID;
  private String entryName;
  private String mappingFit;


}