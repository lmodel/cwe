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
  One change made to an entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweModification  {

  private String modificationName;
  private String modificationOrganization;
  private LocalDate modificationDate;
  private String modificationVersion;
  private LocalDate modificationReleaseDate;
  private String modificationImportance;
  private String modificationComment;


}