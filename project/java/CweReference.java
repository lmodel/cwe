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
  A citation of an external reference from an entry or from one of its parts.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweReference  {

  private CweExternalReference externalReferenceID;
  private String section;


}