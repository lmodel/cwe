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
  A real case of a weakness, usually a CVE record.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweObservedExample  {

  private String reference;
  private String description;
  private URI link;
  private List<String> rationale;


}