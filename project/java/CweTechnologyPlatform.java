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
  A technology where a weakness can appear, named or by its family.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweTechnologyPlatform  {

  private String name;
  private String class_;
  private String prevalence;
  private String note;


}