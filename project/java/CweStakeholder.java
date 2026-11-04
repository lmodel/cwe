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
  A group of people who may find a view useful.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweStakeholder  {

  private String type;
  private String description;


}