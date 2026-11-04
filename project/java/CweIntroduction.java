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
  One way a weakness can get into a product.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweIntroduction  {

  private List<String> phase;
  private List<CweCustomPhase> customPhase;
  private String note;


}