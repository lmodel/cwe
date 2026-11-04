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
  One release of the CWE List, with all its entries and the sources they cite.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweWeaknessCatalog  {

  private String name;
  private String version;
  private LocalDate date;
  private List<CweWeakness> weaknesses;
  private List<CweGrouping> groupings;
  private List<CweView> views;
  private List<CweExternalReference> externalReferences;


}